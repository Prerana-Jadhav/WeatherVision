from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Count
from django.utils import timezone
from datetime import timedelta
from .models import WeatherRecord
from .serializers import WeatherRecordSerializer, WeatherRecordCreateSerializer
from .services import OpenWeatherMapService


class WeatherRecordViewSet(viewsets.ModelViewSet):
    """ViewSet for CRUD operations on WeatherRecord."""
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return WeatherRecordCreateSerializer
        return WeatherRecordSerializer

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Get the latest weather record."""
        latest_record = self.queryset.first()
        if latest_record:
            serializer = self.get_serializer(latest_record)
            return Response(serializer.data)
        return Response({'detail': 'No weather records found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def by_city(self, request):
        """Get weather records filtered by city."""
        city = request.query_params.get('city')
        if not city:
            return Response({'detail': 'Please provide a city parameter.'}, status=status.HTTP_400_BAD_REQUEST)
        records = self.queryset.filter(city__icontains=city)
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def fetch_from_api(self, request):
        """Fetch current weather data from OpenWeatherMap API and save it."""
        city = request.data.get('city')
        if not city:
            return Response({'detail': 'City parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            weather_service = OpenWeatherMapService()
            weather_data = weather_service.get_current_weather(city)
            weather_record = WeatherRecord.objects.create(
                city=weather_data['city'],
                country=weather_data.get('country', ''),
                temperature=weather_data['temperature'],
                humidity=weather_data['humidity'],
                pressure=weather_data['pressure'],
                description=weather_data['description'],
                wind_speed=weather_data['wind_speed'],
                wind_direction=weather_data.get('wind_direction'),
                api_source='openweathermap'
            )
            serializer = self.get_serializer(weather_record)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get statistical analysis of weather data."""
        queryset = self.queryset
        city = request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__icontains=city)

        days = request.query_params.get('days')
        if days:
            try:
                days = int(days)
                date_from = timezone.now() - timedelta(days=days)
                queryset = queryset.filter(recorded_at__gte=date_from)
            except ValueError:
                return Response({'detail': 'Invalid days parameter. Must be a number.'}, status=status.HTTP_400_BAD_REQUEST)

        if not queryset.exists():
            return Response({'detail': 'No data found for the specified filters.'}, status=status.HTTP_404_NOT_FOUND)

        stats = queryset.aggregate(
            avg_temperature=Avg('temperature'),
            max_temperature=Max('temperature'),
            min_temperature=Min('temperature'),
            avg_humidity=Avg('humidity'),
            avg_pressure=Avg('pressure'),
            total_records=Count('id')
        )
        return Response(stats)


def visualization_view(request):
    """View for displaying weather data visualization."""
    return render(request, 'weather/visualization.html', {
        'city': request.GET.get('city', ''),
        'days': request.GET.get('days', '7'),
    })

