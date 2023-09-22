from django.db import models
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
    user = models.IntegerField()
    animal = models.ForeignKey(animals.models.Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
