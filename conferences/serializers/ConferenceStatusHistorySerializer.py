from email.policy import default
from pyexpat import model
from rest_framework import serializers

from ..models import ConferneceStatusHistory

class ConferenceStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ConferneceStatusHistory
        fields='__all__'