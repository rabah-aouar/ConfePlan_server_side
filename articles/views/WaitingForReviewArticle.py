from articles.models.Article import Article
from re import search
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from users.models import User

class WaitingForReviewArticle(ModelViewSet):
    ''' get the list of articles for searcher
    '''
    #get list of articles for the searcher
    serializer_class = ArticleDetailSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return self.request.user.reviewrs_of_article.all()