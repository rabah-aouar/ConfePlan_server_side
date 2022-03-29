from email.mime import image
import site
from statistics import mode
from tkinter import CASCADE
from tkinter.tix import Balloon
from turtle import title
from unicodedata import category
from django.db import models
from users.models import User

# Create your models here.
class Conference(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=600,blank=False)
    #categories=
    start_date=models.DateTimeField( null=True)
    end_date=models.DateTimeField(null= True)
    location=models.CharField(max_length=255)
    site=models.CharField(max_length=500)
    image=models.ImageField()
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='conference_creator')
    reviewers=models.ManyToManyField(User,related_name='conference_reviewers')
    applied_personnes=models.ManyToManyField(User,related_name='conference_applied_personnes')

    
    def __str__(self):
        return(self.title)
