from rest_framework import viewsets

from competitions.models import Competition
from competitions.serializers import CompetitionSerializer
from utils.pagination import CustomPagination, CustomListView


class CompetitionViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    pagination_class = CustomPagination
