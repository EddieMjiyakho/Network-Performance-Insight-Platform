from django.db import models

class NetworkPerformanceData(models.Model):
    date = models.DateField()
    clientCountry = models.CharField(max_length=255)
    clientCity = models.CharField(max_length=255)
    clientRegion = models.CharField(max_length=255)
    clientASN = models.CharField(max_length=255)
    avg_download_speed = models.FloatField()
    avg_upload_speed = models.FloatField()
    avg_latency = models.FloatField()
    africa_regions = models.CharField(max_length=255)

class ASN(models.Model):
    asn = models.CharField(max_length=255, unique=True)

class AfricaRegion(models.Model):
    africa_region_name = models.CharField(max_length=255, unique=True)

class Country(models.Model):
    country_name = models.CharField(max_length=255)

class Region(models.Model):
    region_name = models.CharField(max_length=255)

class City(models.Model):
    city_name = models.CharField(max_length=255)