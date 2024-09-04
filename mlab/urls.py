from . import views
from django.urls import path
from .views import get_country_download_speeds

urlpatterns = [
    path('', views.index, name='index'),
    path('api/country-download-speeds/', get_country_download_speeds, name='country-download-speeds')
]