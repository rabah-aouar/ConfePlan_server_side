from email.policy import default
from pyexpat import model
from rest_framework import serializers

from ..models import ConferenceDatesHistory

class ConferenceDatesHistorySerializer(serializers.ModelSerializer):
    date_of_modification=serializers.ReadOnlyField()
    class Meta:
        model=ConferenceDatesHistory
        fields='__all__'