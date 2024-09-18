from django.urls import path
from . import views

urlpatterns = [
    path('isp-data/', views.get_filtered_data, name='isp_data'),
]
