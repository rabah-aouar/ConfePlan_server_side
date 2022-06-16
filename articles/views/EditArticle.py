from datetime import datetime
from rest_framework import status
from articles.models.Article import Article
from articles.models.RequestToEdit import RequestToEdit
from articles.serializers.ArticleDatesHistorySerializer import ArticleDatesHistorySerializer
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from articles.serializers.EditArticleSerializer import EditArticleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

from notifications.models import notification

class EditArticle(GenericAPIView):
    """end point to post the edited article
    you have to specify the id of the article that you will edited 
    you have to specify the id of the request_to_edit_article 
    """

    serializer_class=EditArticleSerializer
    #parser_classes = (FormParser, MultiPartParser)
    def post(self, request,id):
            serializer= EditArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                #try:
                    article=Article.objects.get(id=id)
                    request_to_edit=serializer.validated_data['request_to_edit']
                    #if request to edit article deadline not passed than edit else deadline has passed
                    if request_to_edit.deadline.replace(tzinfo=None)> datetime.now().replace(tzinfo=None):
                        article.article_url=serializer.validated_data['article_url']
                        article.save()
                        notification.objects.create(subject= "article of title "+str(article.title)+" had modified ",
                        type='normal',invitation_status="pending",users=request_to_edit.user)
                        return Response(data={'article_url':article.article_url.url},status=status.HTTP_201_CREATED)
                    else:
                        return Response(data={'deadline has passed'},status=status.HTTP_400_BAD_REQUEST)
                #except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)