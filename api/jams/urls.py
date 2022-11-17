from django.urls import path
from .views import SongsAPIView, ArtistsAPIView, Ma

urlpatterns = [
    path('songs/', SongsAPIView.as_view()),
    path('songs/<str:pk>/', SongsAPIView.as_view()),
    path('artists/', ArtistsAPIView.as_view()),
    path('artists/<str:pk>/', ArtistsAPIView.as_view()),
    path('managers/')
]