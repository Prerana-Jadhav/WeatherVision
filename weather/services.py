import requests
from django.conf import settings


class OpenWeatherMapService:
    """Service for interacting with OpenWeatherMap API."""
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = settings.OPENWEATHER_API_URL

    def get_current_weather(self, city):
        """Fetch current weather data for a city."""
        if not self.api_key or self.api_key == 'your-api-key-here':
            raise Exception('OpenWeatherMap API key is not configured. Please set OPENWEATHER_API_KEY environment variable.')

        url = f"{self.base_url}/weather"
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return {
                'city': data['name'],
                'country': data['sys'].get('country', ''),
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind'].get('speed', 0),
                'wind_direction': data['wind'].get('deg'),
            }
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch weather data: {str(e)}")
        except KeyError as e:
            raise Exception(f"Unexpected API response format: {str(e)}")
