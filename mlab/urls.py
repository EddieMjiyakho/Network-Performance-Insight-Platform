from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
