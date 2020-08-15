from django.db import models
from django.contrib.auth.models import User


class Donor(models.Model):
    email = models.EmailField()

    first_name = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    country     = models.CharField(max_length=50)
    
    contact_me = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, default="Anonymous")
    comment = models.TextField()

    def __str__(self):
        return self.username


class Blog(models.Model):
    file = models.FileField(upload_to='blog/')


class Assignment(models.Model):
    file = models.FileField(upload_to='assignment/')


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email