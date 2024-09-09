from . import views
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('network-data-filtered/', views.network_data_filtered, name='network_data_filtered'),

    # New URL pattern for region-based filtering
    path('region-data-filtered/', views.region_data_filtered, name='region_data_filtered'),
]