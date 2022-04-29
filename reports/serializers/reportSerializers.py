from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from reports.models.Report import Question, Report


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question','response']
        
class ReportSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Report
        fields = ['id','remark','date_of_submition','score','review_done','user','article','question']
