
from datetime import datetime
from pyexpat import model
from rest_framework import serializers

from reports.models.ReportsModels import Answer, Report
from reports.serializers.AnswerSerializer import AnswerSerializer
from users.models import User


class ReportSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Report
        fields = ['id','user','remark','date_of_submition','score','review_done','article','answers']
    def create(self, validated_data):
        answers = validated_data.pop('answers')
        report = Report.objects.create(**validated_data)
        report.save()
        for answr in answers:
            try:
                tmp = Answer.objects.create(**answr)
                report.answers.add(tmp)
            except:
                print("ooopsieee")
        return report
    
    def update(self,instance,validated_data):
        #update the report + questions
        new_answers = validated_data.pop('answers')
        instance.remark = validated_data.get('remark',instance.remark)
        instance.date_of_submition = datetime.now()
        instance.score = validated_data.get('score',instance.score)
        instance.review_done = validated_data.get('review_done',instance.review_done)
        instance.article = validated_data.get('article',instance.article)
        for answr in new_answers:
            for i in instance.answers.all():
                if i.question.question == answr['question'].question:
                    i.answer = answr.get('answer',i.answer)
                    print(i.answer)
                    i.save()
        instance.save()
        return instance