from django.shortcuts import render
from .entities import *
from mlab.models import NetworkPerformanceData  # 
from django.core.management.base import BaseCommand

metrics = NetworkPerformanceData.objects.all()  # object for the db table

countries = []

def index(request):
    return render(request, 'index.html')
