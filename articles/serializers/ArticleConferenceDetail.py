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
from reports.models.ReportsModels import Answer, Question, Report
from reports.serializers.AnswerSerializer import AnswerSerializer
from reports.serializers.QuestionSerializer import QuestionSerializer
from reports.serializers.ReportSerializer import ReportSerializer
from users.models import User

from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer

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
class reviewersr(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','family_name']

class AnsweranSerializer(serializers.ModelSerializer):
    question=QuestionSerializer()
    class Meta:
        model = Answer
        fields = ['id','question','answer']
class ReportsrSerializer(serializers.ModelSerializer):
    answers = AnsweranSerializer(many=True)
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Report
        fields = ['id','remark','user','date_of_submition','score','review_done','article','answers']

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
    reviewers=reviewersr(many=True)
    report_set=ReportsrSerializer(many=True)
    class Meta:
        model= Article
        fields=['id','title','description','article_url','categories','conference_id','user_id','date_of_creation','last_modification','status','authors','reviewers','report_set']