import datetime
from telnetlib import STATUS
from django.db import models

from users.models import User


invitation_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
]
# Create your models here.
class notification(models.Model):
    subject=models.CharField(max_length=500,null=False)
    date_of_creation=models.CharField(max_length=100,default=datetime.datetime.now)
    type=models.CharField(max_length=20,null=False)
    invitation_status=models.CharField(max_length=30,blank=True,null=True,choices=invitation_status_choices,default='pending')
    conference_id=models.PositiveIntegerField()
    request_to_edit_article_id=models.CharField(max_length=100,blank=True,null=True)
    users_list=models.ManyToManyField(User)