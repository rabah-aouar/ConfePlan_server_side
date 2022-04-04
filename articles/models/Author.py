from datetime import datetime
import uuid
from django.db import models

class Author(models.Model):
    id=models.CharField(default=uuid.uuid4,editable=False,primary_key=True,max_length=255)
    first_name=models.CharField(max_length=255,blank=False,null=False)
    last_name=models.CharField(max_length=255,blank=False,null=False)
    email=models.EmailField(unique=True,blank=False,null=False)