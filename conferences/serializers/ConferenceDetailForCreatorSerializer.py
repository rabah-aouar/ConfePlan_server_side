from email.policy import default
from pyexpat import model
from rest_framework import serializers
from ..models import Conference

class ConferenceDetailForCreatorSerializer(serializers.ModelSerializer):
    #creator=serializers.PrimaryKeyRelatedField()
    #reviewers=serializers.PrimaryKeyRelatedField(many=True,allow_null=True,read_only=True)
    #applied_personnes=serializers.PrimaryKeyRelatedField(many=True,allow_null=True,read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Conference
        fields='__all__'