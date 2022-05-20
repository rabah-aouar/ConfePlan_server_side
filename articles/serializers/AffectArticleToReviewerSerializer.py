from email.policy import default
from pyexpat import model
from rest_framework import serializers

from articles.models.Article import Article, ArticleDatesHistory
from users.models import User

class AffectArticleToReviewerSerializer(serializers.Serializer):
    article=serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(),many=False)
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)