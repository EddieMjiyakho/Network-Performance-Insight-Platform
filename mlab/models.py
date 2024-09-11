from django.db import models

# dataset from measurement-lab.cloudflare.speedtest_speed1
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

# dataset from measurement-lab.ndt.unified_downloads
class ndt_unified_downloads(models.Model):
    test_time = models.TimeField()
    throughput = models.FloatField()  # MeanThroughputMbps
    min_rtt = models.FloatField()  # MinRTT
    packet_loss = models.FloatField()  # LossRate
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    accuracy_radius_km = models.FloatField()
    isp_number = models.IntegerField()  # ASNumber
    isp = models.CharField(max_length=255)  # ASName

    def __str__(self):
        return f"{self.date} - {self.city} ({self.isp})"
    
# dataset from measurement-lab.ndt.unified_uploads
class ndt_unified_uploads(models.Model):
    test_time = models.TimeField()
    throughput = models.FloatField()  # MeanThroughputMbps
    min_rtt = models.FloatField()  # MinRTT
    packet_loss = models.FloatField()  # LossRate
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    accuracy_radius_km = models.FloatField()
    isp_number = models.IntegerField()  # ASNumber
    isp = models.CharField(max_length=255)  # ASName

    def __str__(self):
        return f"{self.date} - {self.city} ({self.isp})"