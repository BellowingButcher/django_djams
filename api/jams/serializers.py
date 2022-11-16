from rest_framework import serializers
from .models import Songs, Artists, Genres, Albums, Playlists, Managers, AlbumsSongs, ArtistsSongs, PlaylistsSongs

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'

class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'

class ManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = '__all__'

class AlbumsSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumsSongs
        fields = '__all__'

class ArtistsSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistsSongs
        fields = '__all__'

class PlaylistsSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistsSongs
        fields = '__all__'