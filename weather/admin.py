from django.contrib import admin
from .models import WeatherRecord


@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    list_display = ['city', 'country', 'temperature', 'humidity', 'description', 'recorded_at']
    list_filter = ['city', 'country', 'recorded_at', 'api_source']
    search_fields = ['city', 'country', 'description']
    readonly_fields = ['recorded_at']
    date_hierarchy = 'recorded_at'

