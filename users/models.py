
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    phone_number=models.CharField(max_length=255)
    full_adress=models.CharField(max_length=255)
    linked_in_username=models.CharField(max_length=255)
    fields_of_interssts=models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
