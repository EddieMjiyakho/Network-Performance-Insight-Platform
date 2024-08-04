import requests
from django.core.management.base import BaseCommand
from mlab.models import RipeData
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetches data from the RIPE Atlas API and stores it in the database'

    def add_arguments(self, parser):
        parser.add_argument('--start_time', type=str, help='Start time for the data fetch', required=True)
        parser.add_argument('--end_time', type=str, help='End time for the data fetch', required=True)
        parser.add_argument('--limit', type=int, default=10, help='Limit the number of results')
        parser.add_argument('--api_key', type=str, required=True, help='API key for RIPE Atlas')

    def handle(self, *args, **kwargs):
        start_time = kwargs['start_time']
        end_time = kwargs['end_time']
        limit = kwargs['limit']
        api_key = kwargs['api_key']

        # Ensure the start_time and end_time are in the correct format
        try:
            start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ").isoformat() + 'Z'
            end_time = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ").isoformat() + 'Z'
        except ValueError:
            self.stdout.write(self.style.ERROR("Start time and End time must be in the format YYYY-MM-DDTHH:MM:SSZ"))
            return

        url = "https://atlas.ripe.net/api/v2/measurements"
        params = {
            "start_time": start_time,
            "end_time": end_time,
            "format": "json",
            "limit": limit,
            "api_key": api_key
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            for record in data:
                RipeData.objects.create(
                    probe_id=record.get('probe', {}).get('id'),
                    measurement_id=record.get('measurement_id'),
                    timestamp=record.get('timestamp'),
                    result=record.get('result')
                )
            self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to retrieve data: {response.status_code} - {response.text}"))
