from articles.models.Article import Article
from django.db import models
from articles.models.Author import Author
from rest_framework import serializers

from conferences.models import Conference
article_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
    ('accepted to review','accepted to review')
]
class ChangeArticleStatusSerializer(serializers.ModelSerializer):
    status=serializers.ChoiceField(required=False,choices=article_status_choices)
    class Meta:
        model= Article
        fields=['status']