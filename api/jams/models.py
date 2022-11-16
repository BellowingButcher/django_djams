from django.db import models

class Songs(models.Model):
    title = models.CharField(max_length=50)
    duration = models.FloatField(default=0)
    plays = models.BigIntegerField(default=0)

class Artists(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(default='Bio goes here')
    img_url = models.URLField(max_length=200, default=None)

class Genres(models.Model):
    keyword = models.CharField(max_length=20, unique=True)

class Albums(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Playlists(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Managers(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=254, unique=True)