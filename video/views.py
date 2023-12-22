import requests
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import Video, Weather7Daily, Weather24Hourly
from .serializers import VideoSerializers


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class WeatherViewSet:
    def get_weekly_weather(self):
        lat = 40.5  # Yarim atrofda joylashgan geografik enlem
        lon = 68.75  # Yarim atrofda joylashgan geografik boylam
        api_key = "f5acb50ac7e17eac9343767377447ac4"
        base_url = f"https://api.openweathermap.org/data/2.5/onecall"
        params = {
            'lat': lat,
            'lon': lon,
            'units': 'metric',
            'exclude': 'current,minutely',
            'appid': api_key,
        }

        response = requests.get(base_url, params=params)
        weather_data = response.json()
        if response.status_code == 200:
            daily_forecast = weather_data.get('daily')[:7]
            Weather7Daily.objects.create(weather=daily_forecast)
            return JsonResponse({'success': 'Success'}, status=200)
        else:
            return JsonResponse({'error': 'weather error'}, status=400)

    def get_hourly_weather(self):
        lat = 40.5  # Yarim atrofda joylashgan geografik enlem
        lon = 68.75  # Yarim atrofda joylashgan geografik boylam
        api_key = "f5acb50ac7e17eac9343767377447ac4"
        base_url = f"https://api.openweathermap.org/data/2.5/onecall"
        params = {
            'lat': lat,
            'lon': lon,
            'units': 'metric',
            'exclude': 'current,minutely,daily',
            'appid': api_key,
        }

        response = requests.get(base_url, params=params)
        weather_data = response.json()
        if response.status_code == 200:
            hourly_forecast = weather_data.get('hourly')[:24]
            Weather24Hourly.objects.create(weather=hourly_forecast)
            return JsonResponse({'success': 'Success'}, status=200)
        else:
            return JsonResponse({'error': 'weather error'}, status=400)
