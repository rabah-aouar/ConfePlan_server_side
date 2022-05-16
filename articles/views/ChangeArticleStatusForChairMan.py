from ast import Delete
from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models.Article import Article, ArticleStatus
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

class ChangeArticleStatusForChairMan(GenericAPIView):
    """end point to change the status oof the article
    """
    serializer_class=ChangeArticleStatusSerializer
    parser_classes = (FormParser, MultiPartParser)
    #accpte article status='accepted'
    #refuse article status='refused'
    #by default pending
    #only the chair man have the permission th change the status 
    def put(self, request ,id):
            accepted=ArticleStatus.objects.get_or_create(status='accepted')
            accepted_id=accepted[0].id
            refused=ArticleStatus.objects.get_or_create(status='refused')
            refused_id=refused[0].id
            accepted_to_review=ArticleStatus.objects.get_or_create(status='accepted to review')
            accepted_to_review_id=accepted_to_review[0].id
            serializer=ChangeArticleStatusSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            try:
                Article1=Article.objects.get(id=id)
                if request.user == Article1.conference_id.creator: 
                    Article1.status=serializer.validated_data['status']
                    Article1.save()
                    if serializer.data.get('status')=="accepted":
                        sr5=ArticleStatusHistorySerializer(data={"type" :accepted_id,"Article":id})
                    elif serializer.data.get('status')=="refused":
                        sr5=ArticleStatusHistorySerializer(data={"type" :refused_id,"Article":id})
                    elif serializer.data.get('status')=="accepted to review":
                        sr5=ArticleStatusHistorySerializer(data={"type" :accepted_to_review_id,"Article":id})
                    sr5.is_valid(raise_exception=True)
                    sr5.save()


                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({"you have not permission to change the status of the article"},status=status.HTTP_400_BAD_REQUEST)
            except:
                #conference doesn't exist(wrong id)
                return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request , id):
        try:
            Article1=Article.objects.get(id=id)
            return Response(data=ArticleDetailSerializer(Article1).data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
