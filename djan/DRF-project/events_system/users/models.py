from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()
    unread_messages = models.TextField()

    class Meta:
        app_label = 'users' 
