from datetime import datetime
from pyexpat import model
from django.db import models
from articles.models.Article_Author import Article_Author
from conferences.models import Conference, DateType
from users.models import User


class Article(models.Model):
    title=models.CharField(max_length=255,blank=False)
    description=models.TextField(max_length=2000,blank=False)
    categories=models.CharField(max_length=2000,blank=False)
    article_url=models.FileField(upload_to='articles',blank=False,null=True)
    date_of_creation=models.DateTimeField(default=datetime.now,editable=False)
    accepted_to_published_by_researchers=models.BooleanField(default=False)
    last_modification=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=30,blank=True,default='waiting for authors')
    conference_id=models.ForeignKey(Conference,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    authors=models.ManyToManyField(to="articles.Author",through=Article_Author)
    reviewers=models.ManyToManyField(User,related_name="reviewrs_of_article")
    
class ArticleDatesHistory(models.Model):
    date_of_modification=models.DateTimeField(max_length=100,default=datetime.now,editable=False)
    Article=models.ForeignKey(Article,on_delete=models.CASCADE)

class ArticleStatus(models.Model):
    status=models.CharField(max_length=100)
    
class ArticleStatusHistory(models.Model):
    date_of_modification=models.DateTimeField(max_length=100,default=datetime.now,editable=False)
    Article=models.ForeignKey(Article,on_delete=models.CASCADE)
    type=models.ForeignKey(ArticleStatus,on_delete=models.CASCADE)