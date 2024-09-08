from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index')
    path('',views.network_data_filtered, name='network_data_filtered')
]