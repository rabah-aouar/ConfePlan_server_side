from email.policy import default
from pyexpat import model
from rest_framework import serializers

from articles.models.Article import ArticleStatusHistory

class ArticleStatusHistorySerializer(serializers.ModelSerializer):
    date_of_modification=serializers.ReadOnlyField()
    class Meta:
        model=ArticleStatusHistory
        fields='__all__'