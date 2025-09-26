from django.urls import include, path
from rest_framework import routers

from events.router import EventViewSet

router = routers.DefaultRouter()
router.register('', EventViewSet, basename='events')

app_name = 'events'
urlpatterns = [
    path('', include(router.urls)),
]
