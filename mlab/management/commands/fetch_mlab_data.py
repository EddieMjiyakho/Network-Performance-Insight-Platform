# Script to fetch data from the M-Lab API and stores it in the database

import requests
from django.core.management.base import BaseCommand
from mlab.models import MLabData

class Command(BaseCommand):
    help = 'Fetches data from the M-Lab API and stores it in the database'

    # Define the API endpoint and parameter
    def handle(self, *args, **kwargs):
        url = "https://api.measurementlab.net/v1/ndt/tcpinfo"
        params = {
            "start_time": "2023-01-01T00:00:00Z",  # Example start time
            "end_time": "2023-01-02T00:00:00Z",    # Example end time
            "format": "json",                      # Response format
            "limit": 10                            # Number of results
        }

        # Make the request to M-Lab API
        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            for record in data:
                MLabData.objects.create(
                    test_id=record.get('test_id'),
                    download_throughput=record.get('download_throughput'),
                    upload_throughput=record.get('upload_throughput'),
                    latency=record.get('latency')
                )
            self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to retrieve data: {response.status_code}"))

