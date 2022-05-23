from ast import Delete
from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models.Article import Article, ArticleStatus
from articles.serializers.AffectArticleToReviewerSerializer import AffectArticleToReviewerSerializer
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from articles.serializers.ArticleStatusHistorySerializer import ArticleStatusHistorySerializer
from conferences.models import Conference
from users.models import User
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView
from articles.serializers.ChangeArticleStatusSerializer import ChangeArticleStatusSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from articles.models.Article import Article

class removeReviewerfromArticleReviewersView(GenericAPIView):
    """
    remove reviewer from article reviewwers
    """
    serializer_class=AffectArticleToReviewerSerializer
    #parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.validated_data["user"]
            article=serializer.validated_data["article"]
            article.reviewers.remove(user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_200_OK)