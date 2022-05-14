from random import choices
from rest_framework import serializers
from ..models import Conference, User

conference_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
]
class AccepteConferenceSerializer(serializers.ModelSerializer):
    status=serializers.ChoiceField(required=True,choices=conference_status_choices)
    class Meta:
        model= Conference
        fields=['status']