from django.db import models
from django.contrib.auth.models import User as User2

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length = 264,unique = True)
    
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.PROTECT)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)
    
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete = models.PROTECT)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
    
class User(models.Model):
    name = models.CharField(max_length = 264)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class UserPortfolio(models.Model):
    user = models.OneToOneField(User2,on_delete = models.PROTECT)
    
    portfolio = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = "profile_pics",blank = True)
    
    def __str__(self):
        return self.user.username