from reports.models.ReportsModels import Question
from rest_framework import serializers



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question','conference']
