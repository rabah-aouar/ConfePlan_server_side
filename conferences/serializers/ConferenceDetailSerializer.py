from pyexpat import model
from rest_framework import serializers
from ..models import Conference
from django.db import models

class ConferenceDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=255,required=False)
    description=serializers.CharField(max_length=255,required=False)
    categories=serializers.CharField(max_length=255,required=False)
    start_date=serializers.CharField(max_length=255,required=False)
    end_date=serializers.CharField(max_length=255,required=False)
    location=serializers.CharField(max_length=255,required=False)
    site=serializers.CharField(max_length=255,required=False)
    logo=serializers.ImageField(required=False)
    class Meta:
        model= Conference
        fields=['id','title','description','categories','start_date','end_date','location','site','logo']

