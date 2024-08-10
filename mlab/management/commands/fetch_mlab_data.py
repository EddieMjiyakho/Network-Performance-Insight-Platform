# network/management/commands/fetch_data.py

from django.core.management.base import BaseCommand
from google.cloud import bigquery
from mlab.models import NetworkPerformance 

class Command(BaseCommand):
    help = 'Fetch data from BigQuery and insert into PostgreSQL'

    def handle(self, *args, **kwargs):
        query = """
            SELECT
            date,
            clientCountry,
            clientASN,
            -- Calculate average for download.bps array and round to 2 decimal places
            ROUND(
                (
                SELECT
                    AVG(value)
                FROM
                    UNNEST(download.bps) AS value
                ), 2
            ) AS avg_download_speed,
            -- Calculate average for upload.bps array and round to 2 decimal places
            ROUND(
                (
                SELECT
                    AVG(value)
                FROM
                    UNNEST(upload.bps) AS value
                ), 2
            ) AS avg_upload_speed,
            -- Calculate average for latencyMs array and round to 2 decimal places
            ROUND(
                (
                SELECT
                    AVG(value)
                FROM
                    UNNEST(latencyMs) AS value
                ), 2
            ) AS avg_latency
            FROM
            `measurement-lab.cloudflare.speedtest_speed1`
            WHERE
            clientCountry IN ('AD', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CG', 'CD', 'DJ', 'EG', 'GQ', 'ER', 'SZ', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'SH', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW')
            AND date >= '2023-01-01' AND date <= '2023-12-31'
            ORDER BY
            date ASC
            LIMIT 100;
        """

        client = bigquery.Client()
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            NetworkPerformance.objects.update_or_create(
                date=row.date,
                clientCountry=row.clientCountry,
                clientASN=row.clientASN,
                defaults={
                    'avg_download_speed': row.avg_download_speed,
                    'avg_upload_speed': row.avg_upload_speed,
                    'avg_latency': row.avg_latency,
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and inserted data'))
