from csv import field_size_limit
from dataclasses import fields
import email
from email.policy import default
from secrets import choice
from turtle import title
from typing_extensions import Required
from django.forms import SlugField
from rest_framework import serializers

from articles.models.Article import Article
from django.db import models
from articles.models.Author import Author

from conferences.models import Conference

class AuthorSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=255,required=True)
    last_name=serializers.CharField(max_length=255,required=True)
    email=serializers.EmailField(max_length=255,required=True)
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


article_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
]
class ArticleDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=True)
    description=serializers.CharField(max_length=255,required=True)
    categories=serializers.CharField(max_length=255,required=True)
    article_url=serializers.FileField(required=False)
    #date_of_creation=serializers.DateTimeField(required=False)
    #last_modification=serializers.DateTimeField(required=False)
    #status=serializers.ChoiceField(required=False,default='pending',choices=article_status_choices)
    conference_id=serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all(),many=False)
    #authors=AuthorSerializer(many=True,required=False,allow_null=True)
    class Meta:
        model= Article
        fields=['id','title','description','categories','article_url','conference_id','authors']
    
    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        article = Article.objects.create(**validated_data)
        article.save
        for author_data in authors_data:
            try:
                author1=Author.objects.get(email=author_data['email'])
                article.authors.add(author1)
                #send email to author contain id of article and his id 
            except:
                a=Author.objects.create(**author_data)
                article.authors.add(a)
        return article