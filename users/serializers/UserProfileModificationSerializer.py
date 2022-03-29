
from rest_framework import serializers
from ..models import User

class UserProfileModificationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255,required=False)
    family_name = serializers.CharField(max_length=255,required=False)
    phone_number=serializers.CharField(max_length=255,required=False)
    full_adress=serializers.CharField(max_length=255,required=False)
    linked_in_username=serializers.CharField(max_length=255,required=False)
    fields_of_interssts=serializers.CharField(max_length=255,required=False)
    bio=serializers.CharField(max_length=1000,default='this is bio',required=False)
    class Meta:
        model= User
        fields=['first_name','family_name','phone_number','full_adress','linked_in_username','fields_of_interssts','bio','profile_picture']