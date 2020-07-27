"""Music views."""

# Django
from django.shortcuts import render
from django.views.generic import ListView

# Models
from spotify.playLists.models import PlayLists


def search(request):
    """View search"""
    track = {
        'title': 'Artist Test',
        'album': 'Album Title',
        'artist': 'Artist Name',
        'duration': '00:00',
    }
    artist = {
        'artist': 'Artist Name',
        'followers': '000000',
        'gene': 'Rock',
        'popular': '000'
    }
    album = {
        'artist': 'Artist Name',
        'market': 'LATAM',
    }
    context = {
        'track': track,
        'artist': artist,
        'album': album,
    }

    return render(
        request=request,
        template_name='music/search.html',
        context=context,
    )


"""
def myLibrary(request):
    data = [
        {
            'num': '1',
            'title': 'Title 1',
            'is_favorite': 'false',
            'duration': '00:00:00',
        },
        {
            'num': '2',
            'title': 'Title 2',
            'is_favorite': 'false',
            'duration': '00:00:00',
        },
        {
            'num': '3',
            'title': 'Title 3',
            'is_favorite': 'true',
            'duration': '00:00:00',
        },
        {
            'num': '4',
            'title': 'Title 4',
            'is_favorite': 'false',
            'duration': '00:00:00',
        },
    ]

    return render(
        request=request,
        template_name='music/myLibrary.html',
        context={'data': data}
    )"""


class MyLibrary (ListView):
    """Display list user favorite Library."""
    model = PlayLists
    context_object_name = 'MyLibrary'
    template_name = 'music/myLibrary.html'

    def get_queryset(self):
        q = PlayLists.objects.filter(user__username=self.kwargs['username'])
        return q


def play(request):
    data = {
        'title': 'Title',
        'album': 'Album',
        'artist': 'Artist Name',
        'duration': '00:00:00',
    }

    return render(
        request=request,
        template_name='music/play.html',
        context={'data': data},
    )


def save():
    pass


"""
def favorite(request):
    data = [
        {
            'title': 'title song',
            'artist': 'Artist name',
            'album': 'Album name',
            'duration': 'minutes',
            'is_favorite': 'true',
        },
        {
            'title': 'title song 2',
            'artist': 'Artist name 2',
            'album': 'Album name 2',
            'duration': 'minutes 2',
            'is_favorite': 'true',
        },
        {
            'title': 'title song 3',
            'artist': 'Artist name 3',
            'album': 'Album name 3',
            'duration': 'minutes 3',
            'is_favorite': 'true',
        },
        {
            'title': 'title song 4',
            'artist': 'Artist name 4',
            'album': 'Album name 4',
            'duration': 'minutes 4',
            'is_favorite': 'true',
        },
    ]
    return render(
        request=request,
        template_name='music/favorites.html',
        context={'data': data}
    )"""


class Favorites (ListView):
    """Display list user favorite songs."""
    model = PlayLists
    context_object_name = 'my_favorites'
    template_name = 'music/favorites.html'

    def get_queryset(self):
        q = PlayLists.objects.filter(user__username=self.kwargs['username'], is_favorite=True)
        return q
