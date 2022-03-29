
# Create your models here.
from distutils.command.upload import upload
from pyexpat import model
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager



# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email adress')
        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_email_verified=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id=models.CharField(max_length=255,default=uuid.uuid4,primary_key=True,editable=False)
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    full_adress=models.CharField(max_length=255)
    linked_in_username=models.CharField(max_length=255)
    fields_of_interssts=models.CharField(max_length=255)
    bio=models.CharField(max_length=1000,default='this is bio',editable=True)
    profile_picture=models.ImageField(upload_to='profile_pictures',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_email_verified=models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin