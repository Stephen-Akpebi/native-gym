# Developed by Surfa
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"publish")
)

class Trainers(models.Model):
    title = models.CharField(max_length=200, unique=False)
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    fb_account = models.CharField(max_length=200, unique=True)
    youtube_account = models.CharField(max_length=200, unique=True)
    insta_account = models.CharField(max_length=200, unique=True)
    twitter_account = models.CharField(max_length=200, unique=True)
    trainer_email = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title

class Trainer(models.Model):
    title = models.CharField(max_length=200, unique=False)
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    fb_account = models.CharField(max_length=200, unique=True)
    youtube_account = models.CharField(max_length=200, unique=True)
    insta_account = models.CharField(max_length=200, unique=True)
    twitter_account = models.CharField(max_length=200, unique=True)
    trainer_email = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    website =  models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

User = get_user_model()

class Bmi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user
    