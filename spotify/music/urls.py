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
        route='favorites/',
        view=views.Favorites.as_view(),
        name='myFavorite'
    ),
    path(
        route='playMusic/',
        view=views.play,
        name='playMusic'
    ),
    path(
        route='myLibrary/',
        view=views.MyLibrary.as_view(),
        name='myLibrary'
    ),
]
