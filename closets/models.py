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
    def __unicode__(self):              # __unicode__ on Python 2
      return self.name

class Item(models.Model):
    closet = models.ForeignKey(Closet)
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    CATEGORY = (
        ('A', 'Accessory'),
        ('T', 'Top'),
        ('B', 'Bottom'),
        ('F', 'Footwear'),
        ('O', 'Other'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY)
    photo = models.ImageField(upload_to='items')
    def __unicode__(self):              # __unicode__ on Python 2
      return self.name
