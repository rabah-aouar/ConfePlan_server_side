from email.policy import default
from pyexpat import model
from rest_framework import serializers

from articles.models.Article import ArticleDatesHistory

class ArticleDatesHistorySerializer(serializers.ModelSerializer):
    date_of_modification=serializers.ReadOnlyField()
    class Meta:
        model=ArticleDatesHistory
        fields='__all__'