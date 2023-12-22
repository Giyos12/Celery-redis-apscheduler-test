from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import VideoViewSet

router = DefaultRouter()
router.register(r'video', VideoViewSet, basename='video')

urlpatterns = router.urls
