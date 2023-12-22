from apscheduler.schedulers.background import BackgroundScheduler
from video.views import WeatherViewSet


def start():
    scheduler = BackgroundScheduler()
    weather = WeatherViewSet()
    scheduler.add_job(weather.get_weekly_weather, 'cron', hour=16, minute=57, second=0, timezone='UTC',
                      id='weatherweakly_001', replace_existing=True)

    scheduler.start()


def start2():
    scheduler = BackgroundScheduler()
    weather = WeatherViewSet()
    scheduler.add_job(weather.get_hourly_weather, 'cron',month=1, hour=0, minute=0, second=0, timezone='UTC',
                      id='weatherhourly_001', replace_existing=True)

    scheduler.start()
