from django.urls import include, path
from . import views

urlpatterns = [
    path('api/', include('api.urls')),  # 
    path('', views.index, name='index'),  # Catch-all for React routes
]