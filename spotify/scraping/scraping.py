
import requests
import json
import time
from random import randint


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
    random_number = randint(0,1995)
    artist_name = artist_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q':'year:0000-9999', 'type':'artist', 'market':'MX', 'limit':4, 'offset':random_number}
    search_params_pre = {'q':'year:0000-9999', 'type':'artist', 'market':'MX'}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search_pre = requests.get(url_search, headers = header, params = search_params_pre)
    search = requests.get(url_search, headers = header, params = search_params)

    if search.status_code == 200:
        result_search_artist_name = search.json()

        result ={'image_url': 'none','artist': 'none', 'followers': 0, 'genres':'none', 'popularity':0}
        result['image_url'] = result_search_artist_name['artists']['items'][0]['images'][1]['url']
        result['artist'] = result_search_artist_name['artists']['items'][0]['name']
        result['followers'] = result_search_artist_name['artists']['items'][0]['followers']['total']
        result['genres'] = result_search_artist_name['artists']['items'][0]['genres'][0]
        result['popularity']= result_search_artist_name['artists']['items'][0]['popularity']
        result_json =json.dumps(result)
        return result_json

    else:
        print(search.status_code)
        print('Request invalid')
    


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

    if search.status_code == 200:
        result_search_track_name = search.json()

        result ={'image_url':'none','title': 'none','artist': 'none', 'album':'none', 'duration':0}
        result['image_url'] = result_search_track_name['tracks']['items'][0]['album']['images'][1]['url']
        result['title'] = result_search_track_name['tracks']['items'][0]['name']
        result['artist'] = result_search_track_name['tracks']['items'][0]['artists'][0]['name']
        result['album'] = result_search_track_name['tracks']['items'][0]['album']['name']
        duration_time = result_search_track_name['tracks']['items'][0]['duration_ms']
        result['duration'] = time.strftime("%M:%S", time.gmtime(duration_time/1000))
        result_json =json.dumps(result)
        return result_json

    else:
        print('Request invalid')



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
    result_search_show_name = search.json()['tracks']['items']['name']

    return result_search_show_name


def get_info_search_bar(looking_for, token):
    looking_for = looking_for.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = { 'q': looking_for,'type':'track,artist,album','market':'MX', 'limit':1, 'offset':0}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_bar = search.json()

    return result_search_bar




if __name__ == '__main__':

    token = get_token()
    """looking_for = input('Que artista buscas? ')
    print(get_info_search_bar(looking_for, token)) """
    """track_name = input('Que cancion buscas? ')
    print(get_info_by_track_name(track_name, token)) """
    artist_name = input('Que artista buscas? ').replace(' ', '+')
    print(get_info_by_artist_name(artist_name, token))
    """playlist_name = input('Que playlist buscas? ').replace(' ', '+')
    print(get_info_by_playlist_name(playlist_name, token))
    show_name = input('Que show buscas? ').replace(' ', '+')
    print(get_info_by_show_name(show_name, token)) """
