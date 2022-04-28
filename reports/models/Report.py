import datetime
from django.db import models
from articles.models.Article import Article

from users.models import User

class Report(models.Model):
    remark=models.CharField(max_length=2000,blank=False,null=False)
    date_of_submition=models.DateTimeField(max_length=100,default=datetime.datetime.now,editable=False)
    score=models.PositiveBigIntegerField(max_length=3000,blank=False,null=False)
    review_done=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    #question=ManyToManyField(Question,related_name='report_question')