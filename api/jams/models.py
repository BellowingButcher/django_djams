from django.db import models

class Songs(models.Model):
    title = models.CharField(max_length=50)
    duration = models.FloatField(default=0)
    plays = models.BigIntegerField(default=0)
    is_explicit = models.BooleanField(default=False)
    # artist_id = models.ForeignKey('Artists', default=None, on_delete=models.CASCADE)
    # playlist_id = models.ForeignKey('Playlists', default=None, on_delete=models.CASCADE)

class Artists(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(default='Bio goes here')
    img_url = models.URLField(max_length=200, default=None)
    # manager_id = models.ForeignKey('Managers', default=None, on_delete=models.CASCADE)
class Genres(models.Model):
    keyword = models.CharField(max_length=20, unique=True)

class Albums(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Playlists(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Managers(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=254, unique=True)

class AlbumsSongs(models.Model):
    song_id = models.ForeignKey(Songs, default=None, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Albums, default=None, on_delete=models.CASCADE)

