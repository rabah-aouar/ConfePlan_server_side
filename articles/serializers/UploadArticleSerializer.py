from distutils.command.upload import upload
from rest_framework import serializers
from articles.models.Article import Article
class UploadArticleSerializer(serializers.ModelSerializer):
    article_url = serializers.FileField(required=True)
    class Meta:
        model=Article
        fields=["article_url"]