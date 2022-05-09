
import datetime
from rest_framework import serializers
from articles.models.Article import Article
from articles.models.RequestToEdit import RequestToEdit

class RequestToEditSerializer(serializers.ModelSerializer):
    modification=serializers.CharField(required=True)
    deadline=serializers.DateTimeField(required=True)
    article=serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(),many=False,required=True)
    class Meta:
        model=RequestToEdit
        exclude=['user','date_of_creation']