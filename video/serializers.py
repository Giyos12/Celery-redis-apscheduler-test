from rest_framework import serializers
from .models import Video, ProxyVideo
from .tasks import creat_proxy_video


class ProxyVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProxyVideo
        fields = '__all__'


class VideoSerializers(serializers.ModelSerializer):
    proxy_videos = ProxyVideoSerializers(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        video = Video.objects.create(**validated_data)
        creat_proxy_video.delay(video.file.name, video.id)
        return video
