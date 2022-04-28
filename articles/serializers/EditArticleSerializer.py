from distutils.command.upload import upload
from rest_framework import serializers
from articles.models.Article import Article
from articles.models.RequestToEdit import RequestToEdit

class EditArticleSerializer(serializers.ModelSerializer):
    article_url = serializers.FileField(required=True)
    request_to_edit=serializers.PrimaryKeyRelatedField(queryset=RequestToEdit.objects.all(),many=False,required=True)
    class Meta:
        model=Article
        fields=["article_url","request_to_edit"]