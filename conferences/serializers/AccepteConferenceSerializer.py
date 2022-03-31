from rest_framework import serializers
from ..models import User

class AccepteConferenceSerializer(serializers.ModelSerializer):
    status=serializers.CharField(required=True)
    class Meta:
        model= User
        fields=['status']