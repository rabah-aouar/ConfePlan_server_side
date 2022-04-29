from pyexpat import model
from rest_framework import serializers

from users.models import User
from ..models import Conference
from django.db import models
class ConferenceModificationSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=False)
    description=serializers.CharField(max_length=255,required=False)
    categories=serializers.CharField(max_length=255,required=False)
    start_date=serializers.DateTimeField(required=False)
    end_date=serializers.DateTimeField(required=False)
    submition_deadline=serializers.DateTimeField(required=False)
    location=serializers.CharField(max_length=255,required=False)
    site=serializers.CharField(max_length=255,required=False)
    name_of_host=serializers.CharField(max_length=255,required=False)
    logo=serializers.ImageField(required=False)
    reviewers=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=True,allow_null=True,required=False)
    pending_articles=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=True,allow_null=True,required=False)
    accepted_articles=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=True,allow_null=True,required=False)
    class Meta:
        model=Conference
        exclude=['creator','status']