"""Music URL's."""

# Django
from django.urls import path

# Views
from spotify.music import views


urlpatterns = [
    # Management
    path(
        route='mylist/',
        view=views.search_music,
        name='myList'
    ),
]
