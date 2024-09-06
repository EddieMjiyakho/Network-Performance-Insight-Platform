import json
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from .models import NetworkPerformanceData, AfricaRegion, ASN

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

    # Prepare data for the pie chart
    pie_chart_data = {
        'labels': countries,
        'datasets': [
            {
                'label': 'Number of ASNs',
                'data': asn_counts,
                'backgroundColor': ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)']
            }
        ]
    }

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
        'pie_chart': pie_chart_data
    }

    # Convert chart_data to JSON and ensure it's safe for JavaScript
    chart_data_json = json.dumps(chart_data)

    return render(request, 'network_data_filtered_list.html', {
        'chart_data': chart_data_json,
        'africa_regions': AfricaRegion.objects.all(),
    })