from pyexpat import model
from rest_framework import serializers

from users.models import User
from ..models import Conference
from django.db import models

class ConferenceDetailSerializer(serializers.ModelSerializer):
    start_date=serializers.DateTimeField()
    end_date=serializers.DateTimeField()
    submition_deadline=serializers.DateTimeField()
    start_submition_date=serializers.DateTimeField()
    status=serializers.ReadOnlyField()
    #creator=serializers.ReadOnlyField()
    #reviewers=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=True,required=False)
    class Meta:
        model= Conference
        fields=['id','title','description','name_of_host','categories','start_date','end_date','submition_deadline','start_submition_date','location','site','logo','status','creator','reviewers']

