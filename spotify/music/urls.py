"""Music URL's."""

# Django
from django.urls import path

# Views
from spotify.music import views


urlpatterns = [
    # Management
    path(
        route='search/',
        view=views.search,
        name='search'
    ),
    path(
        route='my-favorites/',
        view=views.favorite,
        name='myFavorite'
    ),
    path(
        route='playMusic/',
        view=views.play,
        name='playMusic'
    ),
    path(
        route='detailMusic/',
        view=views.myLibrary,
        name='myLibrary'
    ),
]
