from django.core.management.base import BaseCommand
from mlab.models import NetworkPerformanceData

class Command(BaseCommand):
    help = 'Print all network performance metrics'

    def handle(self, *args, **kwargs):
        metrics = NetworkPerformanceData.objects.all()
        total_records = metrics.count()
        
        for metric in metrics:
            self.stdout.write(
                f"Date: {metric.date}, Download Speed: {metric.avg_download_speed}, "
                f"Upload Speed: {metric.avg_upload_speed}, Latency: {metric.avg_latency}, "
                f"Client City: {metric.clientCity}, Client Region: {metric.clientRegion}, "
                f"Client ASN: {metric.clientASN}, Client Country: {metric.clientCountry}"
            )
        
        # Print the total number of records at the end
        self.stdout.write(f"\nTotal number of records: {total_records}")
