from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=notification
        exclude=['users_list']