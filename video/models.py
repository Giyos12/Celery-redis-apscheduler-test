from django.db import models
from django.utils import timezone


class Video(models.Model):
    file = models.FileField(upload_to='videos/')

    @property
    def proxy_videos(self):
        return ProxyVideo.objects.filter(original=self)


class ProxyVideo(models.Model):
    original = models.ForeignKey(Video, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos')
    size = models.IntegerField()


class Weather7Daily(models.Model):
    weather = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'weather7_daily'
        verbose_name = 'Weather7Daily'
        verbose_name_plural = 'Weather7Dailys'


class Weather24Hourly(models.Model):
    weather = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'weather24_hourly'
        verbose_name = 'Weather24Hourly'
        verbose_name_plural = 'Weather24Hourlys'
