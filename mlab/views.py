import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import NetworkPerformanceData, AfricaRegion, ASN, Region

def network_data_filtered(request):
    africa_region_name = request.GET.get('africa_region', None)
    if africa_region_name:
        queryset = NetworkPerformanceData.objects.filter(africa_regions=africa_region_name)
    else:
        queryset = NetworkPerformanceData.objects.all()

    countries = list(queryset.values_list('clientCountry', flat=True).distinct())

    avg_download_speeds = [queryset.filter(clientCountry=country).first().avg_download_speed for country in countries]

    avg_upload_speeds = [queryset.filter(clientCountry=country).first().avg_upload_speed for country in countries]

    avg_latencies = [queryset.filter(clientCountry=country).first().avg_latency for country in countries]

    # Counting ASNs per country
    asn_counts = []
    for country in countries:
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
        'countries': countries
    })

def region_data_filtered(request):
    # Get the selected Africa region and country from the request
    africa_region_name = request.GET.get('africa_region', None)
    country_name = request.GET.get('country', None)

    # Filter data based on the selected region and country
    if africa_region_name and country_name:
        queryset = NetworkPerformanceData.objects.filter(africa_regions=africa_region_name, clientCountry=country_name)
    else:
        # If no country is selected, do not apply this filter
        queryset = NetworkPerformanceData.objects.none()

    # Get regions based on the selected country
    regions = list(Region.objects.filter(country__country_name=country_name).values_list('region_name', flat=True).distinct())

    # Calculate average metrics for each region
    avg_download_speeds = [
        queryset.filter(clientRegion=region).first().avg_download_speed if queryset.filter(clientRegion=region).exists() else 0
        for region in regions
    ]
    avg_upload_speeds = [
        queryset.filter(clientRegion=region).first().avg_upload_speed if queryset.filter(clientRegion=region).exists() else 0
        for region in regions
    ]
    avg_latencies = [
        queryset.filter(clientRegion=region).first().avg_latency if queryset.filter(clientRegion=region).exists() else 0
        for region in regions
    ]

    # Count ASNs for each region
    asn_counts = [
        ASN.objects.filter(asn__in=queryset.filter(clientRegion=region).values_list('clientASN', flat=True)).count()
        for region in regions
    ]

    # Prepare chart data for JavaScript
    chart_data = {
        'line_chart': {
            'labels': regions,
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
            'labels': regions,
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
            'labels': regions,
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

    return render(request, 'region_data_filtered_list.html', {
        'chart_data': chart_data_json,
        'africa_regions': AfricaRegion.objects.all(),
        'regions': regions
    })