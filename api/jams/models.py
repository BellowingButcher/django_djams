from django.db import models

class Songs(models.Model):
    title = models.CharField(max_length=50)
    duration = models.FloatField(default=0)
    plays = models.BigIntegerField(default=0)

class Artists(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(default='Bio goes here')
    img_url = models.URLField(max_length=200, default=None)