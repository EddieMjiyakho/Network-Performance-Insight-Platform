from django.db import models

# Create your models here.

class MLabData(models.Model):
    test_id = models.CharField(max_length=255)
    download_throughput = models.FloatField()
    upload_throughput = models.FloatField()
    latency = models.FloatField()

    def __str__(self):
        return self.test_id