from rest_framework import status
from articles.models.Article import Article
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from articles.serializers.UploadArticleSerializer import UploadArticleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

class UploadArticleView(GenericAPIView):
    """ end point to upload the article 
        you have too specify the id of the article
        if the article is successfuly uploaded response status 200 body url of the article
            if the article id is not valid response status 404 
        else response status 400 
        """
    serializer_class=UploadArticleSerializer
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request,id):
        try:
            serializer= UploadArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                try:
                    article=Article.objects.get(id=id)
                    article.article_url=serializer.validated_data['article_url']
                    article.save()
                    return Response(data={'article_url':article.article_url.url},status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
        except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            # save the creator in db