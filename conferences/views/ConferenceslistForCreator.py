from articles.models.Article import Article
from re import search
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from articles.serializers.ArticleConferenceDetail import ArticleConferenceDetail
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from conferences.models import Conference
from conferences.serializers.ConferenceDetailSerializer import ConferenceDetailSerializer

class ConferenceslistForCreator(ModelViewSet):
    ''' get the list of conferences for searcher
    '''
    #get list of articles for the searcher
    serializer_class = ConferenceDetailSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Conference.objects.filter(creator=self.request.user)