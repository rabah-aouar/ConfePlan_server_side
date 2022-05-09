from operator import imod
from django.http import HttpResponseRedirect
from rest_framework import status
from articles.models.Article import Article
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from articles.models.Article_Author import Article_Author
class AccepteToPublishView(GenericAPIView):
    """end point to accepte to publish the article
            you have to specify the author_id and article_id
    """
    permission_classes=()
    serializer_class=None
    def get(self, request,author_id,article_id):
        try:
            article_author=Article_Author.objects.get(article_id=article_id,author_id=author_id)
            article_author.is_accepte_to_publish_article=True
            article_author.save()
            #if all is accepte to publish true than artcile(id).accepted_by_authors=True
            if Article_Author.objects.filter(article_id=article_id).count()==Article_Author.objects.filter(article_id=article_id,is_accepte_to_publish_article=True).count():
                article=Article.objects.get(id=article_id)
                article.accepted_to_published_by_researchers=True
                article.save()
            #redirect to page that provide (you are accepte an article to be reviewed )
            return HttpResponseRedirect(redirect_to='https://www.google.com/?hl=fr')

        except:
            return Response({"detail":"invalid one of ids"},status=status.HTTP_400_BAD_REQUEST)
