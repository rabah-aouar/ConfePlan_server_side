from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','first_name','family_name','email','password']
        #,'phone_number','full_adress','linked_in_username','field_of_intressts']
        extra_kwargs = {'password': {'write_only': True}}