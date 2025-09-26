from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from events.models import Event
from events.serializers import EventSerializer
from utils.pagination import CustomPagination, CustomListView


class EventViewSet(CustomListView, viewsets.ModelViewSet):
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(
            event_date__gte=timezone.now()
        ).order_by('event_date')
