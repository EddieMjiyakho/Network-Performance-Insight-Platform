import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import ASN, AfricaRegion, NetworkPerformanceData, ndt_unified_downloads  # Import your model
from django.db.models import Avg

def map(request):
        country = request.GET.get('country')
        
        if country:
            # Fetch data filtered by country
            isp_data = ndt_unified_downloads.objects.filter(country=country)
            
            # Aggregate packet loss for each ISP in the selected country
            packet_loss_data = isp_data.values('isp').annotate(avg_packet_loss=Avg('packet_loss'))
            
            # Prepare data for the chart
            isp_names = [entry['isp'] for entry in packet_loss_data]
            packet_losses = [entry['avg_packet_loss'] for entry in packet_loss_data]
            
            # Return data as JSON
            response_data = {
                'labels': isp_names,
                'data': packet_losses,
            }
                    # Serialize the dictionary to JSON with no indent (compact format)
            return JsonResponse(json.loads(json.dumps(response_data)), safe=False)

        # Handle GET request or render map page initially
        return render(request, 'map.html')

def index(request):
    return render(request, 'index.html')


# def network_data_filtered(request):
#     africa_region_name = request.GET.get('africa_region', None)

#     if africa_region_name:
#         # Fetch data based on Africa region
#         queryset = NetworkPerformanceData.objects.filter(africa_regions=africa_region_name)
#     else:
#         # Fetch all data
#         queryset = NetworkPerformanceData.objects.all()

#     countries = list(queryset.values_list('clientCountry', flat=True).distinct())
#     regions = list(queryset.values_list('clientRegion', flat=True).distinct())

#     avg_download_speeds = []
#     avg_upload_speeds = []
#     avg_latencies = []
#     asn_counts = []

#     for country in countries:
#         # Add network metrics
#         avg_download_speeds.append(queryset.filter(clientCountry=country).first().avg_download_speed)
#         avg_upload_speeds.append(queryset.filter(clientCountry=country).first().avg_upload_speed)
#         avg_latencies.append(queryset.filter(clientCountry=country).first().avg_latency)

#         # Counting ASNs per country
#         count = ASN.objects.filter(asn__in=queryset.filter(clientCountry=country).values_list('clientASN', flat=True)).count()
#         asn_counts.append(count)


#     chart_data = {
#         'line_chart': {
#             'labels': countries,
#             'datasets': [
#                 {
#                     'label': 'Avg Download Speed',
#                     'data': avg_download_speeds,
#                     'borderColor': 'rgba(75, 192, 192, 1)',
#                     'backgroundColor': 'rgba(75, 192, 192, 0.4)',
#                     'type': 'line'
#                 },
#                 {
#                     'label': 'Avg Upload Speed',
#                     'data': avg_upload_speeds,
#                     'borderColor': 'rgba(153, 102, 255, 1)',
#                     'backgroundColor': 'rgba(153, 102, 255, 0.4)',
#                     'type': 'line'
#                 },
#             ]
#         },
#         'bar_chart': {
#             'labels': countries,
#             'datasets': [
#                 {
#                     'label': 'Avg Latency',
#                     'data': avg_latencies,
#                     'backgroundColor': 'rgba(153, 102, 255, 0.4)',
#                     'type': 'bar'
#                 }
#             ]
#         },
#         'pie_chart': {
#             'labels': countries,
#             'datasets': [
#                 {
#                     'label': 'Number of ASNs',
#                     'data': asn_counts,
#                     'backgroundColor': ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)']
#                 }
#             ]          
#         }
#     }

#     # Convert chart_data to JSON and ensure it's safe for JavaScript
#     chart_data_json = json.dumps(chart_data)

#     return render(request, 'network/network_data_filtered_list.html', {
#         'chart_data': chart_data_json,
#         'africa_regions': AfricaRegion.objects.all(),
#         'countries': countries,
#     })
