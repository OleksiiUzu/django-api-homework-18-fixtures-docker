from django.db import models
from django.contrib.auth.models import User


'''class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
'''


class UserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media_link = models.CharField(max_length=500)
