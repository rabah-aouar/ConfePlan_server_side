from rest_framework import serializers
from ..models import User
from django.db import models

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','first_name','family_name','email','password','phone_number','full_adress','linked_in_username','fields_of_interssts']
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




