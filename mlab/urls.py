from django.urls import path
from . import views

urlpatterns = [
    # Existing URL pattern for filtering network data
    # path('', views.network_data_filtered, name='network_data_filtered'),
    path('', views.map, name='map')
    
]