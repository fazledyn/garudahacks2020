from django.db import models
from django.contrib.auth.models import User

class SiteUser(User):
    cotter_id   = models.CharField(max_length=300)
    user_id    = models.CharField(max_length=300) 
    identifier  = models.EmailField()

