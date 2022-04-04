
from django.db import models


class Article_____(models.Model):
    is_accepte_to_publish_article=models.BooleanField(default=False,null=False)
    article=models.ForeignKey(to="articles.Article",on_delete=models.CASCADE,default=0)
    author=models.ForeignKey(to="articles.Author",on_delete=models.CASCADE,default=0)