"""Music views."""

# Django
from django.shortcuts import render


def search_music(request):
    return render(
        request,
        'music/search.html',
    )


def detali_music(request):
    return render(
        request,
        'music/detail.html',
    )


def play_music(request):
    return render(
        request,
        'music/play.html',
    )


def save_music():
    pass


def favorite_music(request):
    return render(
        request,
        'music/favorites.html',
    )
