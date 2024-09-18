from django.urls import path
from . import views

urlpatterns = [
    path('isp-data/', views.isp_data_api, name='isp_data'),
]
