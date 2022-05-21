from articles.models.Article import Article
from re import search
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from articles.serializers.ArticleConferenceDetail import ArticleConferenceDetail
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ArticleListView(ModelViewSet):
    ''' get the list of articles for chairman
        you have to specify the status of the articles (pending , accepted, refused , waiting fro review)
    '''
    #get list of articles for the creator of the confernce
    serializer_class = ArticleConferenceDetail
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    def get_queryset(self):
        return Article.objects.filter(conference_id__creator=self.request.user,accepted_to_published_by_researchers=True)
