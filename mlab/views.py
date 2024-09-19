import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import ndt_unified_downloads, ndt_unified_uploads  # Import your models
from .models import NetworkPerformanceData, ASN, AfricaRegion
from django.db.models import Avg

def index(request):
    # Check if a city is provided in the GET parameters
    selected_city = request.GET.get('city')
    
    if selected_city:
        # Query data based on the selected city
        data_downloads = ndt_unified_downloads.objects.filter(city=selected_city)
        data_uploads = ndt_unified_uploads.objects.filter(city=selected_city)

        # Aggregate data
        packet_loss_data = data_downloads.values('isp').annotate(avg_packet_loss=Avg('packet_loss'))
        min_rtt_data = data_downloads.values('isp').annotate(avg_min_rtt=Avg('min_rtt'))
        throughput_data_downloads = data_downloads.values('isp').annotate(avg_throughput=Avg('throughput'))
        throughput_data_uploads = data_uploads.values('isp').annotate(avg_upload_throughput=Avg('throughput'))

        # Prepare data for JSON response
        response_data = {
            'labels': [entry['isp'] for entry in packet_loss_data],
            'data': [entry['avg_packet_loss'] for entry in packet_loss_data],
            'minrtt': [entry['avg_min_rtt'] for entry in min_rtt_data],
            'throughputDownload': [entry['avg_throughput'] for entry in throughput_data_downloads],
            'throughputUpload': [entry['avg_upload_throughput'] for entry in throughput_data_uploads]
        }

        # Serialize data to JSON
        response_data_json = json.dumps(response_data)
    else:
        # No city selected; return empty data
        response_data_json = json.dumps({
            'labels': [],
            'data': [],
            'minrtt': [],
            'throughputDownload': [],
            'throughputUpload': []
        })

    # Cities list (can be dynamically fetched if needed)
    cities = ['Cape Town', 'Joburg', 'Durban']

    return render(request, 'index.html', {
        'cities': cities,
        'response_data': response_data_json
    })

def map(request):
    country = request.GET.get('country')
    
    if country:
        # Fetch data filtered by country from downloads
        isp_data_downloads = ndt_unified_downloads.objects.filter(country=country)
        
        # Aggregate packet loss for each ISP in the selected country
        packet_loss_data = isp_data_downloads.values('isp').annotate(avg_packet_loss=Avg('packet_loss'))
        
        # Prepare data for the bar chart
        isp_names = [entry['isp'] for entry in packet_loss_data]
        packet_losses = [entry['avg_packet_loss'] for entry in packet_loss_data]
        
        # Aggregate min RTT for each ISP
        min_rtt_data = isp_data_downloads.values('isp').annotate(avg_min_rtt=Avg('min_rtt'))
        
        # Prepare data for the line chart (Min RTT)
        min_rtt_values = [entry['avg_min_rtt'] for entry in min_rtt_data]
        
        # Aggregate throughput for each ISP
        throughput_data_downloads = isp_data_downloads.values('isp').annotate(avg_throughput=Avg('throughput'))
        
        # Prepare data for the line chart (Throughput Download)
        throughput_download_values = [entry['avg_throughput'] for entry in throughput_data_downloads]
        
        # Fetch data filtered by country from uploads
        isp_data_uploads = ndt_unified_uploads.objects.filter(country=country)
        
        # Aggregate throughput for each ISP in uploads
        throughput_data_uploads = isp_data_uploads.values('isp').annotate(avg_upload_throughput=Avg('throughput'))
        
        # Prepare data for the line chart (Throughput Upload)
        throughput_upload_values = [entry['avg_upload_throughput'] for entry in throughput_data_uploads]
        
        # Return data as JSON
        response_data = {
            'labels': isp_names,
            'data': packet_losses,
            'minrtt': min_rtt_values,
            'throughputDownload': throughput_download_values,
            'throughputUpload': throughput_upload_values
        }
        
        # Serialize the dictionary to JSON with no indent (compact format)
        return JsonResponse(json.loads(json.dumps(response_data)), safe=False)

    # Handle GET request or render map page initially
    return render(request, 'map.html')


def network_data_filtered(request):
    africa_region_name = request.GET.get('africa_region', None)

    if africa_region_name:
        # Fetch data based on Africa region
        queryset = NetworkPerformanceData.objects.filter(africa_regions=africa_region_name)
    else:
        # Fetch all data
        queryset = NetworkPerformanceData.objects.all()

    countries = list(queryset.values_list('clientCountry', flat=True).distinct())
    regions = list(queryset.values_list('clientRegion', flat=True).distinct())

    avg_download_speeds = []
    avg_upload_speeds = []
    avg_latencies = []
    asn_counts = []

    for country in countries:
        # Add network metrics
        avg_download_speeds.append(queryset.filter(clientCountry=country).first().avg_download_speed)
        avg_upload_speeds.append(queryset.filter(clientCountry=country).first().avg_upload_speed)
        avg_latencies.append(queryset.filter(clientCountry=country).first().avg_latency)

        # Counting ASNs per country
        count = ASN.objects.filter(asn__in=queryset.filter(clientCountry=country).values_list('clientASN', flat=True)).count()
        asn_counts.append(count)


    chart_data = {
        'line_chart': {
            'labels': countries,
            'datasets': [
                {
                    'label': 'Avg Download Speed',
                    'data': avg_download_speeds,
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'backgroundColor': 'rgba(75, 192, 192, 0.4)',
                    'type': 'line'
                },
                {
                    'label': 'Avg Upload Speed',
                    'data': avg_upload_speeds,
                    'borderColor': 'rgba(153, 102, 255, 1)',
                    'backgroundColor': 'rgba(153, 102, 255, 0.4)',
                    'type': 'line'
                },
            ]
        },
        'bar_chart': {
            'labels': countries,
            'datasets': [
                {
                    'label': 'Avg Latency',
                    'data': avg_latencies,
                    'backgroundColor': 'rgba(153, 102, 255, 0.4)',
                    'type': 'bar'
                }
            ]
        },
        'pie_chart': {
            'labels': countries,
            'datasets': [
                {
                    'label': 'Number of ASNs',
                    'data': asn_counts,
                    'backgroundColor': ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)']
                }
            ]          
        }
    }

    # Convert chart_data to JSON and ensure it's safe for JavaScript
    chart_data_json = json.dumps(chart_data)

    return render(request, 'network_data_filtered_list.html', {
        'chart_data': chart_data_json,
        'africa_regions': AfricaRegion.objects.all(),
        'countries': countries,
    })
