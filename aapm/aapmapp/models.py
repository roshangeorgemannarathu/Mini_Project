from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class dealer(AbstractUser):
    fullname = models.TextField(max_length=100, default="")
    role = models.TextField(max_length=100, default="")
    
    def __str___(self):
        return self.username
    
'''class customer(AbstractUser):
    fullname = models.TextField(max_length=100, default="")
    phone = models.CharField(max_length=12, default="")
    housename = models.TextField(max_length=100, default="")
    pincode = models.TextField(max_length=10, default="")
    district = models.TextField(max_length=100, default="")
    def __str___(self):
        return self.username'''

