import datetime
from pickle import FALSE
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from articles.models.Article import Article
from users.models import User
from conferences.models import Conference

class Question(models.Model):
    question=models.CharField(max_length=250,blank=False,null=False)
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE)
    def __str__(self):
        return self.question
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.BooleanField(blank=False,null=False)
    

class Report(models.Model):
    remark=models.CharField(max_length=2000,blank=False,null=False)
    date_of_submition=models.DateTimeField(max_length=100,default=datetime.datetime.now(),editable=False)
    score=models.PositiveBigIntegerField(max_length=3000,blank=False,null=False)
    review_done=models.BooleanField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    answers=models.ManyToManyField(Answer)

