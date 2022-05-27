import datetime
from telnetlib import STATUS
from django.db import models
from users.models import User
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync
invitation_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
]
# Create your models here.
class notification(models.Model):
    subject=models.CharField(max_length=500,null=False)
    date_of_creation=models.DateTimeField(max_length=100,default=datetime.datetime.now,editable=False)
    type=models.CharField(max_length=20,null=False)
    invitation_status=models.CharField(max_length=30,blank=True,null=True,choices=invitation_status_choices,default='pending')
    conference_id=models.PositiveIntegerField(blank=True,null=True)
    request_to_edit_article_id=models.CharField(max_length=100,blank=True,null=True)
    users=models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    class Meta:
        ordering=['-date_of_creation']
    

    def save(self, *args,**kwars):
        channel_layer=get_channel_layer()
        print(self.users)
        super(notification,self).save(*args ,**kwars)
        print(self)
        async_to_sync(channel_layer.group_send)(self.users.id, {
        "type": "send_notification",
        "value": self,
        })
