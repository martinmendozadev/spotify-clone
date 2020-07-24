"""Music URL's."""

# Django
from django.urls import path

# Views
from spotify.music import views


urlpatterns = [
    # Management
    path(
        route='search/',
        view=views.search_music,
        name='search'
    ),
    path(
        route='my-favorites/',
        view=views.favorite_music,
        name='myFavorite'
    ),
    path(
        route='playMusic/',
        view=views.play_music,
        name='playMusic'
    ),
    path(
        route='detailMusic/',
        view=views.detali_music,
        name='detailMusic'
    ),
]
