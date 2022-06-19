import datetime
from rest_framework import status
from articles.models.Article import Article
from articles.serializers.ArticleDatesHistorySerializer import ArticleDatesHistorySerializer
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer, ArticleDetailSerializerformodification
from articles.serializers.UploadArticleSerializer import UploadArticleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser


class ModifyArticleView(GenericAPIView):
    serializer_class=ArticleDetailSerializerformodification
    #parser_classes = (FormParser, MultiPartParser)
    def put(self, request,id):
        try:
            serializer= ArticleDetailSerializerformodification(data=request.data)
            if serializer.is_valid(raise_exception=True):
                try:
                    article=Article.objects.get(id=id)
                    print(article.conference_id.submition_deadline.replace(tzinfo=None))
                    print(datetime.datetime.now())
                    if article.conference_id.submition_deadline.replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None):
                        #article.article_url=serializer.validated_data['article_url']
                        article.title=serializer.validated_data['title']
                        article.description=serializer.validated_data['description']
                        article.categories=serializer.validated_data['categories']
                        article.save()
                        sr=ArticleDatesHistorySerializer(data={"Article":id})
                        sr.is_valid()
                        sr.save()
                        return Response(status=status.HTTP_200_OK)
                    else:
                        return Response(data={'deadline has passed'},status=status.HTTP_400_BAD_REQUEST)
                except:
                    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except:
                return Response(status=status.HTTP_400_BAD_REQUEST)