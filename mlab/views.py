from django.shortcuts import render
from mlab import models
from .entities import *
from mlab.models import NetworkPerformanceData
from django.core.management.base import BaseCommand

metrics = NetworkPerformanceData.objects.all()  # object for the db table

countries = []

def index(request):
    return render(request, 'index.html')

def get_country_download_speeds(request):
    # Query the database for average download speeds by country
    data = NetworkPerformanceData.objects.values('clientCountry').annotate(
        avg_download_speed=models.Avg('avg_download_speed')
    ).order_by('clientCountry')

    # Prepare the data for the chart
    countries = [entry['clientCountry'] for entry in data]
    download_speeds = [entry['avg_download_speed'] for entry in data]

    return render({
        'countries': countries,
        'download_speeds': download_speeds,
    })
