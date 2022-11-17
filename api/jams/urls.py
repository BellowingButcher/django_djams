from django.urls import path
from .views import SongsAPIView, ArtistsAPIView, ManagersList, ManagersDetail, AlbumsList, AlbumsDetail, PlaylistsList, PlaylistsDetail, GenresDetail, GenresList, ArtistsSongsList, ArtistsSongsDetail, AlbumsSongsDetail, AlbumsSongsList
from rest_framework.urlpatterns import format_suffix_patterns
# ManagersAPIView,
urlpatterns = [
    path('songs/', SongsAPIView.as_view()),
    path('songs/<str:pk>/', SongsAPIView.as_view()),
    path('artists/', ArtistsAPIView.as_view()),
    path('artists/<str:pk>/', ArtistsAPIView.as_view()),
    # path('managers/', ManagersAPIView.as_view()),
    # path('managers/<str:pk>/', ManagersAPIView.as_view())
    path('managers/', ManagersList.as_view()),
    path('managers/<str:pk>/', ManagersDetail.as_view()),
    path('albums/', AlbumsList.as_view()),
    path('albums/<str:pk>', AlbumsDetail.as_view()),
    path('playlists/', PlaylistsList.as_view()),
    path('playlists/<str:pk>', PlaylistsDetail.as_view()),
    path('genres/', GenresList.as_view()),
    path('genres/<str:pk>', GenresDetail.as_view()),
    path('artistsonglist/', ArtistsSongsList.as_view()),
    path('artistsonglist/<str:pk>', ArtistsSongsDetail.as_view()),
    path('albumsongs/', AlbumsSongsList.as_view()),
    path('albumsongs/<str:pk>', AlbumsSongsDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)