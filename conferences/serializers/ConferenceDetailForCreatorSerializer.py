from email.policy import default
from pyexpat import model
from rest_framework import serializers

from users.models import User
from ..models import Conference

class ConferenceDetailForCreatorSerializer(serializers.ModelSerializer):
    creator=serializers.PrimaryKeyRelatedField(many=False,allow_null=True,read_only=True)
    reviewers=serializers.PrimaryKeyRelatedField(many=True,allow_null=True,read_only=True)
    status=serializers.ReadOnlyField()
    class Meta:
        model=Conference
        fields='__all__'