# Script to fetch data from the M-Lab API and stores it in the database

import requests
from django.core.management.base import BaseCommand
from mlab.models import MLabData

class Command(BaseCommand):
    help = 'Fetches data from the M-Lab API and stores it in the database'
    
    def handle(self, *args, **kwargs):
        url = "https://api.measurementlab.net/v1/ndt/tcpinfo"
        params = {
            "start_time": "2023-01-01T00:00:00Z",  # Example start time
            "end_time": "2023-01-02T00:00:00Z",    # Example end time
            "format": "json",                      # Response format
            "limit": 10                            # Number of results
        }

