
import email
from typing_extensions import Required
from django.forms import CharField, UUIDField
from rest_framework import serializers
from ..models import User
from django.db import models

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['first_name','family_name','email','password','phone_number','full_adress','linked_in_username','fields_of_interssts']
        #password is for write only 
        extra_kwargs = {'password': {'write_only': True}}
    
    #hashed the password when create a new user

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

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

class BlockUserSerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(required=True)
    class Meta:
        model= User
        fields=['is_active']
