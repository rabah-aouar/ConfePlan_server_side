from rest_framework import serializers

from reports.models.ReportsModels import Answer



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','question','answer']
    