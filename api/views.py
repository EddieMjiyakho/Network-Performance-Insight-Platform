from django.http import JsonResponse
from mlab.models import ndt_unified_downloads

def isp_data_api(request):
    # Query the first entry for simplicity, or filter/aggregate based on your needs
    isp_data = ndt_unified_downloads.objects.values(
        'throughput', 
        'min_rtt', 
        'packet_loss', 
        'country', 
        'test_time', 
        'isp'
    ).first()  # Fetch only the first record for now
    
    # Structure the data to be returned as JSON
    data = {
        'throughput': isp_data['throughput'],
        'min_rtt': isp_data['min_rtt'],
        'packet_loss': isp_data['packet_loss'],
        'country': isp_data['country'],
        'test_time': isp_data['test_time'],
        'isp': isp_data['isp'],
    }

    return JsonResponse(data)
