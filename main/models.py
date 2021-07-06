from django.db import models
from datetime import datetime

class Certificate(models.Model):
    title = models.CharField(max_length=50, default='Тут должно быть название')
    description = models.TextField(default='Тут должно быть описание')
    date = models.DateField(default=datetime.now())
    preview = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=50, default='Тут должно быть название')
    description = models.TextField(default='Тут должно быть описание')
    dateStart = models.DateField(default=datetime.now())
    dateEnd = models.DateField(default=datetime.now())
    preview = models.ImageField()

class Project(models.Model):
    title = models.CharField(max_length=50, default='Тут должно быть название')
    description = models.TextField(default='Тут должно быть описание')
    dateStart = models.DateField(default=datetime.now())
    dateEnd = models.DateField(default=datetime.now())
    preview = models.ImageField()

class Tourtaiment(models.Model):
    title = models.CharField(max_length=50, default='Тут должно быть название')
    description = models.TextField(default='Тут должно быть описание')
    date = models.DateField(default=datetime.now())
    place = models.PositiveSmallIntegerField(default=1)
    preview = models.ImageField()