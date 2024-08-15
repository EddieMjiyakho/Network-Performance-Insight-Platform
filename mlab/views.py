from django.shortcuts import render
from rest_framework import viewsets
# from .models import MyModel
# from .serializers import MyModelSerializer
from .entities import *
from mlab.models import NetworkPerformanceData  # 
from django.core.management.base import BaseCommand

metrics = NetworkPerformanceData.objects.all()  # object for the db table


# class MyModelViewSet(viewsets.ModelViewSet):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

countries = []

def show_Metrics(request):
     for metric in metrics:
        if metric.clientCountry == 'ZA':
            metric = NetworkMetric(id=1, metric_name='metric', value=50.0, timestamp=metric.date, country_id=metric.clientCountry, region_id=metric.clientRegion, city_id=metric.clientCity)
            countries.append(metric)

     context = {'metrics': countries}
     return render(request, 'index.html', context)