from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'

    def ready(self):
        from video.weather_scheduling import weather_updater
        weather_updater.start()
        weather_updater.start2()
