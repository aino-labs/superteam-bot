from rest_framework import viewsets

from subscribes.models import Subscribe
from subscribes.serializers import SubscribeSerializer
from utils.pagination import CustomPagination, CustomListView


class SubscribeViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    pagination_class = CustomPagination
