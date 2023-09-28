from django.db import models


class Sex(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=200)
    animal_type = models.CharField(max_length=200)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    age = models.IntegerField()
    breed = models.CharField(max_length=200)
    availability = models.BooleanField()
    description = models.TextField(max_length=500)
    healthy = models.BooleanField()

    def __str__(self):
        return self.name


class AnimalMedia(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    media_link = models.ImageField(upload_to='animals/images')
    main = models.BooleanField()

    def __str__(self):
        return self.animal_id


class Schedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.IntegerField()
