from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User)
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)

class Closet(models.Model):
    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
