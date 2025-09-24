from django.urls import include, path
from rest_framework import routers

from subscribes.router import SubscribeViewSet

router = routers.DefaultRouter()
router.register('', SubscribeViewSet)

app_name = 'subscribes'
urlpatterns = [
    path('', include(router.urls)),
]
