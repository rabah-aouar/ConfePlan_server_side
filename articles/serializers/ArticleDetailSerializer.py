from csv import field_size_limit
from dataclasses import fields
from turtle import title
from typing_extensions import Required
from rest_framework import serializers

from articles.models.Article import Article
from django.db import models
from articles.models.Author import Author

from conferences.models import Conference

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']



class ArticleDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=True)
    description=serializers.CharField(max_length=255,required=True)
    categories=serializers.CharField(max_length=255,required=True)
    #article_url=serializers.FileField(required=False)
    date_of_creation=serializers.DateTimeField(required=False)
    last_modification=serializers.DateTimeField(required=False)
    status=serializers.CharField(required=False)
    conference_id=serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all(),many=False)
    authors=serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),many=True,required=False,allow_null=True)
    class Meta:
        model= Article
        fields=['id','title','description','categories','date_of_creation','last_modification','status','conference_id','authors']