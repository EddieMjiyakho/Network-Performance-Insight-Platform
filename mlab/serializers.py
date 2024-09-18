from rest_framework import serializers
from mlab.models import ndt_unified_downloads

class NetworkPerformanceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ndt_unified_downloads 
        fields = '__all__'  # Use this to include all fields or specify certain fields, e.g. ['field1', 'field2']
