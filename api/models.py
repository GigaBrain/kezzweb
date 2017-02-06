from __future__ import unicode_literals

from django.db import models

# Create your models here.

from mongoengine import *

connect('kezz')

class Signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


