import datetime
from email.policy import default


from django.db import models
#from articles.models.Article import Article
from users.models import User
#from articles.models.Article import Article

# Create your models here.


conference_status_choices = [
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('refused', 'refused'),
]
class Conference(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    date_of_creation=models.DateTimeField(max_length=100,default=datetime.datetime.now,editable=False)
    description=models.TextField(max_length=3000,blank=False,null=False)
    categories=models.CharField(max_length=500,blank=False,null=False)
    name_of_host=models.CharField(max_length=200,blank=False,null=False)
    start_date=models.DateTimeField(max_length=100,blank=False,null=False)
    end_date=models.DateTimeField(max_length=100,blank=False,null=False)
    submition_deadline=models.DateTimeField(max_length=100,blank=False,null=False,default=datetime.datetime.now)
    location=models.CharField(max_length=200,blank=False,null=False)
    site=models.CharField(max_length=200,blank=False,null=False)
    logo=models.ImageField(upload_to='logos',blank=True,default='hello')
    status=models.CharField(max_length=15,default='pending',choices=conference_status_choices)
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='conference_creator',editable=False)
    reviewers=models.ManyToManyField(User,related_name='conference_reviewers')
    #pending_articles=models.ManyToManyField("articles.Article",related_name='conference_pending_articles')
    #accepted_articles=models.ManyToManyField("articles.Article",related_name='conference_accepted_articles')
    class Meta:
        ordering=['-date_of_creation']
    def __str__(self):
        return(self.title)
