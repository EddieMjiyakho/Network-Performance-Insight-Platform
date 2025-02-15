from django.core.management.base import BaseCommand
from google.cloud import bigquery
from mlab.models import NetworkPerformanceData
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
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mlab\\management\\commands\\credits\\glossy-apex-435110-p6-577d38d7c831.json"

        query = """
            SELECT
                date,
                clientCountry,
                clientCity,
                clientRegion,
                clientASN,
                ROUND(AVG(download_speed), 2) AS avg_download_speed,
                ROUND(AVG(upload_speed), 2) AS avg_upload_speed,
                ROUND(AVG(latency), 2) AS avg_latency,
                africa_regions
            FROM (
                SELECT
                    date,
                    clientCountry,
                    clientCity,
                    clientRegion,
                    clientASN,
                    ROUND(
                        (
                        SELECT
                            AVG(value)
                        FROM
                            UNNEST(download.bps) AS value
                        ), 2
                    ) AS download_speed,
                    ROUND(
                        (
                        SELECT
                            AVG(value)
                        FROM
                            UNNEST(upload.bps) AS value
                        ), 2
                    ) AS upload_speed,
                    ROUND(
                        (
                        SELECT
                            AVG(value)
                        FROM
                            UNNEST(latencyMs) AS value
                        ), 2
                    ) AS latency,
                    CASE 
                        WHEN clientCountry IN ('ET', 'ER', 'SO', 'DJ', 'KE', 'TZ', 'UG', 'RW', 'BI', 'SS') THEN 'East Africa'
                        WHEN clientCountry IN ('NG', 'GH', 'SL', 'LR', 'CI', 'TG', 'BJ', 'BF', 'ML', 'GM', 'SN', 'GN', 'GW', 'CV') THEN 'West Africa'
                        WHEN clientCountry IN ('MA', 'DZ', 'TN', 'LY', 'EG', 'SD') THEN 'North Africa'
                        WHEN clientCountry IN ('ZA', 'NA', 'BW', 'LS', 'SZ', 'MZ', 'ZM', 'ZW', 'AO', 'MW') THEN 'Southern Africa'
                        WHEN clientCountry IN ('CM', 'CF', 'TD', 'CG', 'CD', 'GA', 'GQ') THEN 'Central Africa'
                        ELSE 'Other'
                    END AS africa_regions
                FROM
                    `measurement-lab.cloudflare.speedtest_speed1`
                WHERE
                    clientCountry IN ('AD', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CG', 'CD', 'DJ', 'EG', 'GQ', 'ER', 'SZ', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'SH', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW')
                    AND date >= '2023-08-01'
                    AND clientCountry IS NOT NULL AND clientCountry != ''
                    AND clientRegion IS NOT NULL AND clientRegion != ''
                    AND clientCity IS NOT NULL AND clientCity != ''
                    AND clientASN IS NOT NULL AND clientASN > 0
                    AND ARRAY_LENGTH(download.bps) > 0
                    AND ARRAY_LENGTH(upload.bps) > 0
                    AND ARRAY_LENGTH(latencyMs) > 0
                ORDER BY
                    date ASC
                LIMIT 100000
            )
            GROUP BY
                date, clientCountry, clientCity, clientRegion, clientASN, africa_regions
        """

        try:
            # Initialize BigQuery client
            client = bigquery.Client()  # Uses the environment variable for credentials
            query_job = client.query(query)
            results = query_job.result()

            new_records_count = 0
            updated_records_count = 0

            # Process the results from BigQuery
            for row in results:
                obj, created = NetworkPerformanceData.objects.update_or_create(
                    date=row.date,
                    clientCountry=row.clientCountry,
                    clientCity=row.clientCity,
                    clientRegion=row.clientRegion,
                    clientASN=row.clientASN,
                    defaults={
                        'avg_download_speed': row.avg_download_speed,
                        'avg_upload_speed': row.avg_upload_speed,
                        'avg_latency': row.avg_latency,
                        'africa_regions': row.africa_regions,
                    }
                )
                if created:
                    new_records_count += 1
                else:
                    updated_records_count += 1

            # Calculate total records in the database
            total_records_count = NetworkPerformanceData.objects.count()

            # Print results
            self.stdout.write(self.style.SUCCESS(
                f'Successfully fetched data. New records: {new_records_count}, Updated records: {updated_records_count}'
            ))
            self.stdout.write(self.style.SUCCESS(f'Total number of records in the database: {total_records_count}'))

        except Exception as e:
            logging.error(f'Error occurred: {e}')
            self.stdout.write(self.style.ERROR(f'Failed to fetch and insert data: {e}'))

        finally:
            client.close()
