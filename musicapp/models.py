
from django.db import models
from datetime import datetime


# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length= 300)
    date_released = models.DateField(auto_now_add=True)
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length = 300)


class Lyrics(models.Model):
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.CharField(max_length = 500)
    song_id = models.CharField(max_length = 300)