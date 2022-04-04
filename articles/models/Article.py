from datetime import datetime
from django.db import models
from articles.models.Article_Author import Article_____
from conferences.models import Conference
from users.models import User


class Article(models.Model):
    title=models.CharField(max_length=255,blank=False)
    description=models.TextField(max_length=2000,blank=False)
    categories=models.CharField(max_length=2000,blank=False)
    #article_url=models.FileField(upload_to='articles',null=True)
    date_of_creation=models.DateTimeField(default=datetime.now,editable=False)
    accepted_to_published_by_researchers=models.BooleanField(default=False)
    last_modification=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=30,blank=True)
    conference_id=models.ForeignKey(Conference,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    authors=models.ManyToManyField("articles.Author",through=Article_____)