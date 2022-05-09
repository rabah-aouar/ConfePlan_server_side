from articles.models.Article import Article
from re import search
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer

class ArticleListView(ModelViewSet):
    ''' get the list of articles for searcher
    '''
    #get list of articles for the creator of the confernce
    serializer_class = ArticleDetailSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)