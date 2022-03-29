
from rest_framework import serializers
from ..models import User

class BlockUserSerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(required=True)
    class Meta:
        model= User
        fields=['is_active']