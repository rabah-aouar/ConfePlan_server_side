from operator import imod
from rest_framework import status
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from articles.models.Article_Author import Article_____
class AccepteToPublishView(GenericAPIView):
    permission_classes =()
    def post(self, request,author_id,article_id):
        try:
            article_author=Article_____.objects.get(article_id=article_id,author_id=author_id)
            article_author.is_accepte_to_publish_article=True
            article_author.save()
            return Response(status=status.HTTP_200_OK)

            #if all is accepte to publish true than artcile(id)=True
        except:
            return Response({"detail":"invalid one of ids"},status=status.HTTP_400_BAD_REQUEST)
