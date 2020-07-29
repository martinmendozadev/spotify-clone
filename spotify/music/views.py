"""Music views."""

# Django
from django.shortcuts import render
from django.views.generic import ListView

# Models
from spotify.playLists.models import PlayLists

# Utils
import json
from spotify.scraping.scraping import get_info_by_search_name, get_token


def search(request):
    """View search"""
    try:
        data_search = json.loads(get_info_by_search_name(request.GET['search'],  get_token()))
        track = data_search['track']
        artist = data_search['artist']
        album = data_search['album']
        context = {
            'track': track,
            'artist': artist,
            'album': album,
        }
    except:
        context = {
            'track': None,
            'artist': None,
            'album': None,
        }

    return render(
        request=request,
        template_name='music/search.html',
        context=context,
    )


class MyLibrary (ListView):
    """Display list user favorite Library."""
    model = PlayLists
    context_object_name = 'MyLibrary'
    template_name = 'music/myLibrary.html'

    def get_queryset(self):
        q = PlayLists.objects.filter(user__username=self.request.user.username)
        return q


def play(request):
    data = {
        'title': 'BitâKora 5: Marcas en tiempos de COVID, Elon Musk y Bose.',
        'album': 'Podcast',
        'artist': 'Nadia Molina',
        'duration': '47:89:14',
    }

    return render(
        request=request,
        template_name='music/play.html',
        context={'data': data},
    )


def save():
    pass


class Favorites (ListView):
    """Display list user favorite songs."""
    model = PlayLists
    context_object_name = 'my_favorites'
    template_name = 'music/favorites.html'

    def get_queryset(self):
        q = PlayLists.objects.filter(user__username=self.request.user.username, is_favorite=True)
        return q
