from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mlab.models import ndt_unified_downloads
from mlab.serializers import NetworkPerformanceDataSerializer
from django.db.models import Q

@api_view(['GET'])
def get_filtered_data(request):
    try:
        # Get filter parameters from query params in the request
        region = request.query_params.get('region')
        country = request.query_params.get('country')
        isp = request.query_params.get('isp')
        time_range = request.query_params.get('time')

        # Start with all data
        queryset = ndt_unified_downloads.objects.all()

        # Apply filters
        if region:
            queryset = queryset.filter(africa_regions=region)
        
        if country:
            queryset = queryset.filter(clientCountry=country)
        
        if isp:
            queryset = queryset.filter(isp=isp)
        
        if time_range and time_range != 'all':
            start_date, end_date = time_range.split(' to ')
            queryset = queryset.filter(test_time__range=[start_date, end_date])

        # Serialize filtered data
        serializer = NetworkPerformanceDataSerializer(queryset, many=True)

        return Response(serializer.data)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)