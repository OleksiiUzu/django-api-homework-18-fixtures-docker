import datetime
from django.db import models
from django.contrib.auth.models import User
import animals.models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/images')
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    media = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(animals.models.Animal, on_delete=models.CASCADE)
    date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    def __str__(self):
        return self.title
