from rest_framework import serializers
from .models import WeatherRecord


class WeatherRecordSerializer(serializers.ModelSerializer):
    """Serializer for WeatherRecord model."""
    class Meta:
        model = WeatherRecord
        fields = [
            'id', 'city', 'country', 'temperature', 'humidity',
            'pressure', 'description', 'wind_speed', 'wind_direction',
            'recorded_at', 'api_source'
        ]
        read_only_fields = ['id', 'recorded_at']


class WeatherRecordCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating WeatherRecord."""
    class Meta:
        model = WeatherRecord
        fields = [
            'city', 'country', 'temperature', 'humidity',
            'pressure', 'description', 'wind_speed', 'wind_direction',
            'api_source'
        ]
