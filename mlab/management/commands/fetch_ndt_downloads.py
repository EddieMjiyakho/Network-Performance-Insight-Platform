from django.core.management.base import BaseCommand
from google.cloud import bigquery
from mlab.models import ndt_unified_downloads
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help = 'Fetch data from BigQuery and insert into PostgreSQL'

    def handle(self, *args, **kwargs):
        logging.info('Starting data fetch from BigQuery')

        # Set the credentials path if not already set
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mlab\\management\\commands\\credits\\networkperformancedata-8b6857d2f299.json"

        query = """
            SELECT
            id, 
            a.TestTime as TestTime, 
            a.MeanThroughputMbps as Throughput, 
            a.MinRTT as MinRTT, 
            a.LossRate as PacketLoss, 
            client.Geo.CountryName as Country, 
            client.Geo.City as City,
            client.Geo.Latitude as Latitude, 
            client.Geo.Longitude as Longitude, 
            client.Geo.AccuracyRadiusKm as AccuracyRadiusKm, 
            client.Network.ASNumber as ISP_number, 
            client.Network.ASName as ISP
            FROM
            `measurement-lab.ndt.unified_downloads`
            WHERE
            date = '2023-09-02'
            AND client.Geo.ContinentCode ="AF";
        """

        try:
            # Initialize BigQuery client
            client = bigquery.Client()  # Uses the environment variable for credentials
            query_job = client.query(query)
            results = query_job.result()

            new_records_count = 0

            # Process the results from BigQuery
            for row in results:
                # Use create() to add new records
                ndt_unified_downloads.objects.create(
                    test_time=row.TestTime,
                    throughput=row.Throughput,
                    min_rtt=row.MinRTT,
                    packet_loss=row.PacketLoss,
                    country=row.Country,
                    city=row.City,
                    latitude=row.Latitude,
                    longitude=row.Longitude,
                    accuracy_radius_km=row.AccuracyRadiusKm,
                    isp_number=row.ISP_number,
                    isp=row.ISP,
                )
                new_records_count += 1

            # Calculate total records in the database
            total_records_count = ndt_unified_downloads.objects.count()

            # Print results
            self.stdout.write(self.style.SUCCESS(
                f'Successfully fetched data. New records added: {new_records_count}'
            ))
            self.stdout.write(self.style.SUCCESS(f'Total number of records in the database: {total_records_count}'))

        except Exception as e:
            logging.error(f'Error occurred: {e}')
            self.stdout.write(self.style.ERROR(f'Failed to fetch and insert data: {e}'))

        finally:
            client.close()