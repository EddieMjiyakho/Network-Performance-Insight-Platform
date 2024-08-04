# mlab/management/commands/fetch_ripe_data.py
import requests
from django.core.management.base import BaseCommand, CommandError
from mlab.models import RipeAtlasData
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_fixed

class Command(BaseCommand):
    help = 'Fetches data from the RIPE Atlas API and stores it in the database'

    def add_arguments(self, parser):
        parser.add_argument('--start_time', type=str, help='Start time for the data fetch (ISO format)')
        parser.add_argument('--end_time', type=str, help='End time for the data fetch (ISO format)')
        parser.add_argument('--limit', type=int, default=10, help='Number of results to fetch')
        parser.add_argument('--api_key', type=str, required=True, help='RIPE Atlas API key')

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
    def fetch_data(self, url, params, headers):
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def handle(self, *args, **kwargs):
        url = "https://atlas.ripe.net/api/v2/measurements"
        params = {
            "start": kwargs['start_time'],
            "stop": kwargs['end_time'],
            "page_size": kwargs['limit']
        }
        headers = {
            "Authorization": f"Key {kwargs['api_key']}"
        }

        try:
            data = self.fetch_data(url, params, headers)
        except requests.exceptions.RequestException as e:
            raise CommandError(f"Error fetching data from RIPE Atlas API: {e}")
        except ValueError as e:
            raise CommandError(f"Error decoding JSON response: {e}")

        for record in data['results']:
            RipeAtlasData.objects.create(
                probe_id=record['probe']['id'],
                measurement_id=record['id'],
                result=record['result'],
                timestamp=datetime.fromtimestamp(record['timestamp'])
            )

        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
