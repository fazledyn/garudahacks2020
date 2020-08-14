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


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email