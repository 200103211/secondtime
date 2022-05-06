from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.


class log(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField (max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm = models.CharField(max_length=100)