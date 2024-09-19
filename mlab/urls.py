from django.urls import include, path
from . import views

urlpatterns = [
    # path('api/', include('api.urls')),  # 
    # path('', views.index, name='index'),  # Catch-all for React routes

  
    # Existing URL pattern for filtering network data
    # path('', views.network_data_filtered, name='network_data_filtered'),
    path('', views.map, name='map')

]