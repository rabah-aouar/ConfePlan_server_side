from operator import imod
from django.http import HttpResponseRedirect
from rest_framework import status
from articles.models.Article import Article, ArticleStatus
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from articles.models.Article_Author import Article_Author
from articles.serializers.ArticleStatusHistorySerializer import ArticleStatusHistorySerializer
from notifications.models import notification
class AccepteToPublishView(GenericAPIView):
    """end point to accepte to publish the article
            you have to specify the author_id and article_id
    """
    permission_classes=()
    serializer_class=None
    def get(self, request,author_id,article_id):
        try:
            article_author=Article_Author.objects.get(article_id=article_id,author_id=author_id)
            print(article_author)
            article_author.is_accepte_to_publish_article=True
            article_author.save()
            #if all is accepte to publish true than artcile(id).accepted_by_authors=True
            if Article_Author.objects.filter(article_id=article_id).count()==Article_Author.objects.filter(article_id=article_id,is_accepte_to_publish_article=True).count():
                article=Article.objects.get(id=article_id)
                article.accepted_to_published_by_researchers=True
                article.save()
                pending=ArticleStatus.objects.get_or_create(status='pending')
                pending_id=pending[0].id
                article.status="pending"
                article.save()
                notification.objects.create(subject= "a new article is add to conference "+str(article.conference_id.title),
                type='normal',invitation_status="pending",users=article.conference_id.creator)
                sr5=ArticleStatusHistorySerializer(data={"type" :pending_id,"Article":article.id})
                sr5.is_valid(raise_exception=True)
                sr5.save()
            #redirect to page that provide (you are accepte an article to be reviewed )
            return HttpResponseRedirect(redirect_to='https://www.google.com/?hl=fr')

        except:
            return Response({"detail":"invalid one of ids"},status=status.HTTP_400_BAD_REQUEST)
