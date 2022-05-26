import datetime
from rest_framework import status
from articles.models.Article import Article, ArticleStatus
from articles.serializers.ArticleDatesHistorySerializer import ArticleDatesHistorySerializer
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

from articles.serializers.ArticleStatusHistorySerializer import ArticleStatusHistorySerializer
from conferences.models import Conference

class ArticleView(GenericAPIView):
    """ end point to create an article object 
        response status 200 body object
        else status 400 body errors
    """
    serializer_class=ArticleDetailSerializer
    def post(self, request):
            waiting=ArticleStatus.objects.get_or_create(status='waiting for authors')
            waiting_id=waiting[0].id
            serializer= ArticleDetailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data["conference_id"].submition_deadline.replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None):
                    serializer.validated_data['user_id']=request.user
                    serializer.save()
                    sr=ArticleDatesHistorySerializer(data={"Article":serializer.data['id']})
                    sr.is_valid(raise_exception=True)
                    sr.save()
                    sr5=ArticleStatusHistorySerializer(data={"type" :waiting_id,"Article":serializer.data['id']})
                    sr5.is_valid(raise_exception=True)
                    sr5.save()
                    return Response(data=serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(data={'deadline has passed'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


