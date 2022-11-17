from django.urls import path
from .views import SongsAPIView, ArtistsAPIView, ManagersAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('songs/', SongsAPIView.as_view()),
    path('songs/<str:pk>/', SongsAPIView.as_view()),
    path('artists/', ArtistsAPIView.as_view()),
    path('artists/<str:pk>/', ArtistsAPIView.as_view()),
    path('managers/', ManagersAPIView.as_view()),
    path('managers/<str:pk>/', ManagersAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)