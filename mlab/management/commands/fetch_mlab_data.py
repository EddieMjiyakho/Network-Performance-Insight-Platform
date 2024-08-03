# Script to fetch data from the M-Lab API and stores it in the database

import requests
from django.core.management.base import BaseCommand
from mlab.models import MLabData

class Command(BaseCommand):
    help = 'Fetches data from the M-Lab API and stores it in the database'


