"""
URL configuration for weathervision project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather.urls')),
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]

