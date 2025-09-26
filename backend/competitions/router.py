from rest_framework import viewsets

from competitions.models import Competition
from competitions.serializers import CompetitionSerializer
from utils.pagination import CustomPagination, CustomListView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CompetitionViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    pagination_class = CustomPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
