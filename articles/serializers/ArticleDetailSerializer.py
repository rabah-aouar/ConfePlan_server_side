
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



class ArticleDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=True)
    description=serializers.CharField(max_length=255,required=True)
    categories=serializers.CharField(max_length=255,required=True)
    date_of_creation=serializers.ReadOnlyField()
    last_modification=serializers.ReadOnlyField(required=False)
    status=serializers.ReadOnlyField()
    #status=serializers.ReadOnlyField(required=False,default='pending',choices=article_status_choices)
    conference_id=serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all(),many=False)
    authors=AuthorSerializer(many=True,required=False,allow_null=True)
    user_id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model= Article
        fields=['id','title','description','categories','conference_id','user_id','date_of_creation','last_modification','status','authors']
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
        article.save
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