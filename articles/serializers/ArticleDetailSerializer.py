
from enum import unique
import stat
from telnetlib import STATUS
from typing_extensions import Required
from rest_framework import serializers

from articles.models.Article import Article
from django.db import models
from articles.models.Author import Author
from articles.serializers.ArticleConferenceDetail import AnsweranSerializer
AnsweranSerializer

from conferences.models import Conference
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

from notifications.models import notification

class AuthorSerializer1(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=255,required=True)
    last_name=serializers.CharField(max_length=255,required=True)
    email=serializers.EmailField(max_length=255,required=True)
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']



class ArticleDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=True)
    description=serializers.CharField(max_length=255,required=True)
    categories=serializers.CharField(max_length=255,required=True)
    date_of_creation=serializers.ReadOnlyField()
    last_modification=serializers.ReadOnlyField(required=False)
    status=serializers.ReadOnlyField()
    #status=serializers.ReadOnlyField(required=False,default='pending',choices=article_status_choices)
    conference_id=serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all(),many=False)
    authors=AuthorSerializer1(many=True,required=False,allow_null=True)
    user_id=serializers.StringRelatedField(read_only=True)
    reviewers=serializers.PrimaryKeyRelatedField(many=True,allow_null=True,read_only=True)
    class Meta:
        model= Article
        fields=['id','title','description','article_url','categories','conference_id','user_id','date_of_creation','last_modification','status','authors','reviewers']
        extra_kwargs = {'user_id': {'read_only': True}}
    def send_acceptation_email(email,author_id,article_id):
        verification_page_link='http://127.0.0.1:8000/articles/accepte_to_be_published/'+str(author_id)+'/'+article_id
        subject = 'confirm your account on Confplan'
        message = 'if you accepte to publish your article click on the link \n'+verification_page_link
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        try:
            send_mail( subject, message, email_from, recipient_list )
        except:
            return Response(data={"check your cnx"},status=status.HTTP_400_BAD_REQUEST)
        return

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        article = Article.objects.create(**validated_data)
        article.save()
        if len(authors_data)==0:
            print(len(authors_data))
            article.accepted_to_published_by_researchers=True
            article.status="pending"
            article.save()
            notification.objects.create(subject= "a new article is add to conference "+str(article.conference_id.title),
            type='normal',invitation_status="pending",users=article.conference_id.creator)
        for author_data in authors_data:
            try:
                author1=Author.objects.get(email=author_data['email'])
                article.authors.add(author1)
                ArticleDetailSerializer.send_acceptation_email(author_data['email'],author1.id,str(article.id))
                #send email to author contain id of article and his id 
            except:
                a=Author.objects.create(**author_data)
                article.authors.add(a)
                ArticleDetailSerializer.send_acceptation_email(author_data['email'],a.id,str(article.id))
                #send email to author contain id of article and his id 
        return article


class ArticleDetailSerializerformodification(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=False)
    description=serializers.CharField(max_length=255,required=False)
    categories=serializers.CharField(max_length=255,required=False)
    class Meta:
        model= Article
        fields=['id','title','description','article_url','categories']