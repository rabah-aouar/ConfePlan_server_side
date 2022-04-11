from pyexpat import model
from rest_framework import serializers
from ..models import Conference
from django.db import models

class ConferenceDetailSerializer(serializers.ModelSerializer):
    start_date=serializers.DateTimeField()
    end_date=serializers.DateTimeField()
    class Meta:
        model= Conference
        fields=['id','title','description','name_of_host','categories','start_date','end_date','location','site','logo']

