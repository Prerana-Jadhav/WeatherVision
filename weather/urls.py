from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherRecordViewSet, visualization_view

router = DefaultRouter()
router.register(r'records', WeatherRecordViewSet, basename='weatherrecord')

urlpatterns = [
    path('', include(router.urls)),
    path('visualization/', visualization_view, name='visualization'),
]

