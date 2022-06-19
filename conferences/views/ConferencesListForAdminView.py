from re import search
from rest_framework import status
from conferences.models import Conference
from conferences.serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser

class ConferencesListForAdminView(ModelViewSet):
    ''' get all the conferences to the admin panel'''
    queryset= Conference.objects.filter(status="pending")
    permission_classes = (IsAdminUser ,)
    serializer_class = ConferenceDetailSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'categories']
