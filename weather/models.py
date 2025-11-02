from django.db import models
from django.utils import timezone


class WeatherRecord(models.Model):
    """Model to store weather data records."""
    
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, help_text="Temperature in Celsius")
    humidity = models.IntegerField(help_text="Humidity percentage")
    pressure = models.IntegerField(help_text="Atmospheric pressure in hPa")
    description = models.CharField(max_length=255)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, help_text="Wind speed in m/s")
    wind_direction = models.IntegerField(help_text="Wind direction in degrees", null=True, blank=True)
    recorded_at = models.DateTimeField(default=timezone.now)
    api_source = models.CharField(max_length=50, default='openweathermap', help_text="Source of the weather data")
    
    class Meta:
        ordering = ['-recorded_at']
        indexes = [
            models.Index(fields=['city', '-recorded_at']),
            models.Index(fields=['-recorded_at']),
        ]
    
    def __str__(self):
        return f"{self.city} - {self.temperature}°C - {self.recorded_at.strftime('%Y-%m-%d %H:%M')}"

