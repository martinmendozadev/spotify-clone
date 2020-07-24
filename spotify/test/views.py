"""Test views."""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Utils
from spotify.scraping.scraping import get_info_by_artist_id, get_token


@login_required()
def hello(request):
    """Feed users."""
    token = get_token()
    data = get_info_by_artist_id('bad bunny', token)

    return render(
        request,
        'users/overview-page.html' 
    )
