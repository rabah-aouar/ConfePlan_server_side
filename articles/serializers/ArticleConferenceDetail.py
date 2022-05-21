from enum import unique
import stat
from telnetlib import STATUS
from typing_extensions import Required
from rest_framework import serializers

from articles.models.Article import Article
from django.db import models
from articles.models.Author import Author

from conferences.models import Conference
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

class AuthorSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=255,required=True)
    last_name=serializers.CharField(max_length=255,required=True)
    email=serializers.EmailField(max_length=255,required=True)
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']

class Conferencesr(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ['id', 'title']



class ArticleConferenceDetail(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=True)
    description=serializers.CharField(max_length=255,required=True)
    categories=serializers.CharField(max_length=255,required=True)
    date_of_creation=serializers.ReadOnlyField()
    last_modification=serializers.ReadOnlyField(required=False)
    status=serializers.ReadOnlyField()
    #status=serializers.ReadOnlyField(required=False,default='pending',choices=article_status_choices)
    conference_id=Conferencesr()
    authors=AuthorSerializer(many=True,required=False,allow_null=True)
    user_id=serializers.StringRelatedField(read_only=True)
    reviewers=serializers.StringRelatedField(many=True,allow_null=True,read_only=True)
    class Meta:
        model= Article
        fields=['id','title','description','article_url','categories','conference_id','user_id','date_of_creation','last_modification','status','authors','reviewers']
        extra_kwargs = {'user_id': {'read_only': True}}