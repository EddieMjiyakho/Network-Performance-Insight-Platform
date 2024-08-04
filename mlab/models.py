from django.db import models

# Create your models here.

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