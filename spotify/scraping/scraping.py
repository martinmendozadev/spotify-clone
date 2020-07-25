"""Request Info from Spotify API"""

# Utils
import requests


def get_token():

    token_url = 'https://accounts.spotify.com/api/token'
    params = {'grant_type': 'client_credentials'}
    headers = {'Authorization': 'Basic ODAwMjM3YWRhMWI4NGUxYTlmNTU1YjY3OGIxZGM5Y2I6ZmQxNjA0Y2Q2YzM4NGIzYThlYzA4ZjI4ZDM0NzA2MWU'}
    r = requests.post(token_url, data = params, headers = headers )

    return r.json()['access_token']


def get_info_by_artist_id(artist_id, token):
    ep_artist = '/artists/{artist_id}'
    url_base = 'https://api.spotify.com/v1'
    header = {'Authorization': 'Bearer {}'.format(token)}
    r = requests.get(url_base+ep_artist.format(artist_id = artist_id), headers = header)
    info_by_artist = r.json()

    return info_by_artist


def get_info_by_artist_name(artist_name, token):
    artist_name = artist_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': artist_name, 'type':'artist', 'market':'MX', 'limit':1}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_artist_name = search.json()

    return result_search_artist_name


def get_info_by_album_name(album_name, token):
    album_name = album_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': album_name, 'type':'album', 'market':'MX', 'limit':1}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_album_name = search.json()

    return result_search_album_name


def get_info_by_track_name(track_name, token):
    track_name = track_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': track_name, 'type':'track', 'market':'MX', 'limit':1}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_track_name = search.json()

    return result_search_track_name


def get_info_by_playlist_name(playlist_name, token):
    playlist_name = playlist_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': playlist_name, 'type':'playlist', 'market':'MX', 'limit':1}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_playlist_name = search.json()

    return result_search_playlist_name


def get_info_by_show_name(show_name, token):
    show_name = show_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': show_name, 'type':'show', 'market':'MX', 'limit':1}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_show_name = search.json()

    return result_search_show_name
