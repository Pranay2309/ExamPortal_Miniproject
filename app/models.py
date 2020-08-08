from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    Question_No = models.IntegerField(null=True,blank=True)
    Question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100,null=True,blank=True)

class Answerset(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    Answer1 = models.CharField(max_length=100,null=True,blank=True)
    Answer2 = models.CharField(max_length=100,null=True,blank=True)
    Answer3 = models.CharField(max_length=100,null=True,blank=True)
    Answer4 = models.CharField(max_length=100,null=True,blank=True)
    Answer5 = models.CharField(max_length=100,null=True,blank=True)
    Answer6 = models.CharField(max_length=100,null=True,blank=True)
    Answer7 = models.CharField(max_length=100,null=True,blank=True)
    correct1 = models.BooleanField(null=True,blank=True)
    correct2 = models.BooleanField(null=True,blank=True)
    correct3 = models.BooleanField(null=True,blank=True)
    correct4 = models.BooleanField(null=True,blank=True)
    correct5 = models.BooleanField(null=True,blank=True)
    correct6 = models.BooleanField(null=True,blank=True)
    correct7 = models.BooleanField(null=True,blank=True)
    marks = models.FloatField(null=True,blank=True)