from celery import shared_task
from converter import Converter

from video.models import ProxyVideo, Video

conv = Converter()


@shared_task
def creat_proxy_video(file_name, id):
    size = 240
    proxy_file_name = f'media_root/{file_name}_{size}.mp4'
    convert = conv.convert(f'media_root/{file_name}', proxy_file_name, {
        'format': 'mp4',
        'audio': {
            'codec': 'aac',
            'samplerate': 11025,
            'channels': 2
        },
        'video': {
            'codec': 'hevc',
            'width': size,
            'fps': 25
        }})

    for timecode in convert:
        print(f'\rConverting ({timecode:.2f}) ...')
    instance = Video.objects.get(id=id)

    ProxyVideo.objects.create(original=instance, file=proxy_file_name, size=size)
