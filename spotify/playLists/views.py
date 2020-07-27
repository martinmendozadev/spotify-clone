"""PlayLists views."""

# Django
from django.shortcuts import redirect

# Models
from spotify.music.models import TrackModel
from spotify.playLists.models import PlayLists

# Utils
import json
from spotify.scraping.scraping import get_info_by_search_name, get_token


TOKEN = '123'
TRACK = None


def add_track(request, title):
    """View test"""
    track_exist = search_track(title)
    user = request.user

    if track_exist:
        add_in_user_library(user, TRACK)
    else:
        obtain_token()
        save_track_in_db(title)
        add_in_user_library(user, TRACK)

    return redirect('music:search')


def search_track(title):
    global TRACK
    try:
        TRACK = TrackModel.objects.get(title=title)
        return True
    except TrackModel.DoesNotExist:
        return False


def add_in_user_library(user, track):
    user_have_track = PlayLists.objects.filter(user=user, track=track)

    if not user_have_track.exists():
        PlayLists.objects.create(user=user, track=track)


def save_track_in_db(title):
    global TRACK
    data_track = json.loads(get_info_by_search_name(title, TOKEN))
    TRACK = TrackModel.objects.create(
        artist=data_track['track']['artist'],
        title=data_track['track']['title'],
        album=data_track['track']['album'],
        duration=data_track['track']['duration'],
    )


def obtain_token():
    global TOKEN
    TOKEN = get_token()


def add_favorite_track(request, title):
    PlayLists.objects.filter(user=request.user, track__title=title).update(is_favorite=True)
    return redirect('music:myLibrary')
