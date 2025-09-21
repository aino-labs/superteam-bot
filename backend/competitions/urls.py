from django.urls import include, path
from rest_framework import routers

from competitions.router import CompetitionViewSet

router = routers.DefaultRouter()
router.register('', CompetitionViewSet)

app_name = 'competitions'
urlpatterns = [
    path('', include(router.urls)),
]
