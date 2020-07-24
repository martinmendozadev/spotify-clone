"""Music views."""

# Django
from django.shortcuts import render


def search_music(request):
    track = {
        'image': 'url: album de la track',
        'album': 'title: album',
        'artist': 'artist name',
        'year': 'public year',
        'duration': 'time',
    }

    return render(
        request=request,
        template_name='music/search.html',
        context={'track': track},
    )


def detali_music(request):
    data = [
        {
            'image': 'url: album de la track',
            'name_track': 'name track',
            'is_favorite': 'boolean value',
            'duration': 'time',
        },
        {
            'image': 'url: album de la track 2',
            'name_track': 'name track 2',
            'is_favorite': 'boolean value 2',
            'duration': 'time 2',
        },
        {
            'image': 'url: album de la track 3',
            'name_track': 'name track 3',
            'is_favorite': 'boolean value 3',
            'duration': 'time 3',
        },
        {
            'image': 'url: album de la track 4',
            'name_track': 'name track 4',
            'is_favorite': 'boolean value 4',
            'duration': 'time 4',
        },
    ]

    return render(
        request=request,
        template_name='music/detail.html',
        context={'data': data}
    )


def play_music(request):
    data = {
        'image': 'url: album de la track',
        'name_track': 'name track',
        'album': 'boolean value',
        'duration': 'time',
    }

    return render(
        request=request,
        template_name='music/play.html',
        context={'data': data},
    )


def save_music():
    pass


def favorite_music(request):
    data = [
        {
            'title': 'title song',
            'artist': 'Artist name',
            'album': 'Album name',
            'year': 'Year publish',
            'duration': 'minutes'
        },
        {
            'title': 'title song 2',
            'artist': 'Artist name 2',
            'album': 'Album name 2',
            'year': 'Year publish 2',
            'duration': 'minutes 2'
        },
        {
            'title': 'title song 3',
            'artist': 'Artist name 3',
            'album': 'Album name 3',
            'year': 'Year publish 3',
            'duration': 'minutes 3'
        },
        {
            'title': 'title song 4',
            'artist': 'Artist name 4',
            'album': 'Album name 4',
            'year': 'Year publish 4',
            'duration': 'minutes 4'
        },
    ]
    return render(
        request=request,
        template_name='music/favorites.html',
        context={'data': data}
    )
