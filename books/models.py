import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null= False)

    def __str__(self):
        return self.first_name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publish_date = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)