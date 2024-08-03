from django.db import models

# Create your models here.

class MLabData(models.Model):
    download_throughput = models.FloatField()
    upload_throughput = models.FloatField()
    latency = models.FloatField()

    def __str__(self):
        return self.test_id