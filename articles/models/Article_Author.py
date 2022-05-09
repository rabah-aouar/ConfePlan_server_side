
from django.db import models
from articles.models.Author import Author

class Article_Author(models.Model):
    is_accepte_to_publish_article=models.BooleanField(default=False,null=False)
    article=models.ForeignKey("articles.Article",on_delete=models.CASCADE,default=0)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default=0)