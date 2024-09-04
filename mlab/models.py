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

class NetworkMetric(models.Model):
    asn = models.ForeignKey(ASN, on_delete=models.CASCADE)
    avg_download_speed = models.FloatField()
    avg_upload_speed = models.FloatField()
    avg_latency = models.FloatField()

class AfricaRegion(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    africa_region = models.ForeignKey(AfricaRegion, on_delete=models.CASCADE)
    network_metric = models.ForeignKey(NetworkMetric, on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    network_metric = models.ForeignKey(NetworkMetric, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    client_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    network_metric = models.ForeignKey(NetworkMetric, on_delete=models.CASCADE)

