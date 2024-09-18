from django.urls import include, path
from . import views

urlpatterns = [
    # Existing URL pattern for filtering network data
    # path('', views.network_data_filtered, name='network_data_filtered'),
    # path('', views.map, name='map')
    path('api/', include('api.urls')),  # Your API routes
    path('', views.index),  # Catch-all for React routes
    
]