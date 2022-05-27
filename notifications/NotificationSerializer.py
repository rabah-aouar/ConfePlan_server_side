from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from conferences.models import Conference
from .models import notification
invitation_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
]
class NotificationSerializer(serializers.ModelSerializer):
    invitation_status=serializers.ChoiceField(choices=invitation_status_choices)
    conference_id=serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all(),required=False)
    class Meta:
        model=notification
        exclude=['users']