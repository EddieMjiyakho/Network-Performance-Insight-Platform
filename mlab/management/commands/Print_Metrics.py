from django.core.management.base import BaseCommand
from mlab.models import NetworkPerformanceData  # Replace 'your_app' with your app name

class Command(BaseCommand):
    help = 'Print all network performance metrics'

    def handle(self, *args, **kwargs):
        metrics = NetworkPerformanceData.objects.all()
        for metric in metrics:
            self.stdout.write(
                f"Date: {metric.date}, Download Speed: {metric.avg_download_speed}, "
                f"Upload Speed: {metric.avg_upload_speed}, Latency: {metric.avg_latency}, "
                f"Client ASN: {metric.clientASN}, Client Country: {metric.clientCountry}"
            )
