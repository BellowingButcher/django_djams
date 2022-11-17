from django.db import models

class Songs(models.Model):
    title = models.CharField(max_length=50)
    duration = models.FloatField(default=0)
    plays = models.BigIntegerField(default=0)
    is_explicit = models.BooleanField(default=False)
class Artists(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(default='Bio goes here')
    img_url = models.URLField(max_length=200, default=None, null=True)

class Genres(models.Model):
    keyword = models.CharField(max_length=20, unique=True)

class Albums(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Playlists(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Managers(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=254, unique=True)

class ArtistsManagers(models.Model):
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    manager = models.ForeignKey(Managers, on_delete=models.CASCADE)

class AlbumsSongs(models.Model):
    song = models.ForeignKey(Songs, default=None, on_delete=models.CASCADE)
    album = models.ForeignKey(Albums, default=None, on_delete=models.CASCADE)

class ArtistsSongs(models.Model):
    song = models.ForeignKey(Songs, default=None, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artists, default=None, on_delete=models.CASCADE)

class PlaylistsSongs(models.Model):
    song = models.ForeignKey(Songs, default=None, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlists, default=None, on_delete=models.CASCADE)


