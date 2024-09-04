from django.shortcuts import render
from .entities import *
from mlab.models import NetworkPerformanceData
from django.core.management.base import BaseCommand

metrics = NetworkPerformanceData.objects.all()  # object for the db table

countries = []

def index(request):
    return render(request, 'index.html')

def get_country_download_speeds(request):
    # Query the database for download speeds by country
    data = NetworkPerformanceData.objects.values('clientCountry').order_by('clientCountry')

    # Prepare the data for the chart
    countries = []
    download_speeds = []

    for entry in data:
        countries.append(entry['clientCountry'])
        download_speeds.append(entry['avg_download_speed'])

    return render({
        'countries': countries,
        'download_speeds': download_speeds,
    })
