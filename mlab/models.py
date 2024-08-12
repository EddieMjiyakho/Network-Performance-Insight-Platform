from django.db import models

class MLabData(models.Model):
    download_throughput = models.FloatField()
    upload_throughput = models.FloatField()
    latency = models.FloatField()

    def __str__(self):
        return self.test_id
    
class RipeAtlasData(models.Model):
    probe_id = models.IntegerField()
    measurement_id = models.IntegerField()
    result = models.JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Probe ID: {self.probe_id}, Measurement ID: {self.measurement_id}"

class NetworkPerformance(models.Model):
    date = models.DateField()
    clientCountry = models.CharField(max_length=255)
    clientASN = models.CharField(max_length=255)
    avg_download_speed = models.FloatField()
    avg_upload_speed = models.FloatField()
    avg_latency = models.FloatField()

class NetworkPerformanceData(models.Model):
    date = models.DateField()
    clientCountry = models.CharField(max_length=255)
    clientCity = models.CharField(max_length=255)
    clientRegion = models.CharField(max_length=255)
    clientASN = models.CharField(max_length=255)
    avg_download_speed = models.FloatField()
    avg_upload_speed = models.FloatField()
    avg_latency = models.FloatField()

