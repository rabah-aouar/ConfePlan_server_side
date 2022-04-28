from datetime import datetime
from django.db import models
from users.models import User
from articles.models.Article import Article


class RequestToEdit(models.Model):
    modification=models.TextField(max_length=10000,blank=False,null=False)
    deadline=models.DateTimeField(blank=False,null=False)
    date_of_creation=models.DateTimeField(default=datetime.now,editable=False)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)