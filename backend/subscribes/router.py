from rest_framework.decorators import action
from rest_framework import viewsets, status

from subscribes.models import Subscribe
from subscribes.serializers import SubscribeSerializer
from utils.pagination import CustomPagination, CustomListView
from rest_framework.response import Response


class SubscribeViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['delete'], url_path='by-chat-id/(?P<chat_id>[^/.]+)')
    def delete_by_chat_id(self, request, chat_id=None):
        try:
            subscribe = Subscribe.objects.get(chat_id=chat_id)
            subscribe.delete()
            return Response(
                status=status.HTTP_200_OK
            )
        except Subscribe.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

