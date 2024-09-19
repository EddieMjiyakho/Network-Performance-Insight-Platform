from django.urls import include, path
from .views import map, network_data_filtered, index
from django.shortcuts import render  # Import render function

urlpatterns = [
    # path('api/', include('api.urls')),  # 
    # path('', views.index, name='index'),  # Catch-all for React routes

  
    # Existing URL pattern for filtering network data
    # path('', views.network_data_filtered, name='network_data_filtered'),
    # path('', views.map, name='map')

    # URL pattern for the map view
    path('map/', map, name='map'),

    # URL pattern for the network data filtered view
    path('network-data/', network_data_filtered, name='network_data_filtered'),

    # URL pattern for the index page
    path('', index, name='index'),

]