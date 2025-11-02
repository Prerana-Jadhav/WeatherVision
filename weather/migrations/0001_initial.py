# Generated migration file
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, help_text='Temperature in Celsius', max_digits=5)),
                ('humidity', models.IntegerField(help_text='Humidity percentage')),
                ('pressure', models.IntegerField(help_text='Atmospheric pressure in hPa')),
                ('description', models.CharField(max_length=255)),
                ('wind_speed', models.DecimalField(decimal_places=2, help_text='Wind speed in m/s', max_digits=5)),
                ('wind_direction', models.IntegerField(blank=True, help_text='Wind direction in degrees', null=True)),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('api_source', models.CharField(default='openweathermap', help_text='Source of the weather data', max_length=50)),
            ],
            options={
                'ordering': ['-recorded_at'],
            },
        ),
        migrations.AddIndex(
            model_name='weatherrecord',
            index=models.Index(fields=['city', '-recorded_at'], name='weather_wea_city_abc123_idx'),
        ),
        migrations.AddIndex(
            model_name='weatherrecord',
            index=models.Index(fields=['-recorded_at'], name='weather_wea_recorde_idx'),
        ),
    ]

