
import requests #2.22.0
import json #2.0.9
import time #no tiene
from random import randint #no tiene



def get_token():

    token_url = 'https://accounts.spotify.com/api/token'
    params = {'grant_type': 'client_credentials'}
    headers = {'Authorization': 'Basic ODAwMjM3YWRhMWI4NGUxYTlmNTU1YjY3OGIxZGM5Y2I6ZmQxNjA0Y2Q2YzM4NGIzYThlYzA4ZjI4ZDM0NzA2MWU'}
    r = requests.post(token_url, data = params, headers = headers )

    return r.json()['access_token']



def get_info_by_artist_name(token):
    random_number = randint(0,1995)
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q':'year:0000-9999', 'type':'artist', 'market':'MX', 'limit':4, 'offset':random_number}
    search_params_pre = {'q':'year:0000-9999', 'type':'artist', 'market':'MX'}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search_pre = requests.get(url_search, headers = header, params = search_params_pre)
    search = requests.get(url_search, headers = header, params = search_params)

    if search.status_code == 200:
        result_search_artist_name = search.json()

        result ={
            'artist_0':{
                        'image_url': 'none',
                        'artist': 'none', 
                        'followers': 0, 
                        'genres':'none', 
                        'popularity':0},
            'artist_1':{
                        'image_url': 'none',
                        'artist': 'none', 
                        'followers': 0, 
                        'genres':'none', 
                        'popularity':0},
            'artist_2':{
                        'image_url': 'none',
                        'artist': 'none', 
                        'followers': 0, 
                        'genres':'none', 
                        'popularity':0},
            'artist_3':{
                        'image_url': 'none',
                        'artist': 'none', 
                        'followers': 0, 
                        'genres':'none', 
                        'popularity':0}
                }
        try:
            result['artist_0']['image_url'] = result_search_artist_name['artists']['items'][0]['images'][1]['url']
            result['artist_0']['artist'] = result_search_artist_name['artists']['items'][0]['name']
            result['artist_0']['followers'] = result_search_artist_name['artists']['items'][0]['followers']['total']
            result['artist_0']['genres'] = result_search_artist_name['artists']['items'][0]['genres'][0]
            result['artist_0']['popularity']= result_search_artist_name['artists']['items'][0]['popularity']
        except IndexError as err:
            print('uups, we have a problem with your search, I dare you to try again (つ▀¯▀)つ: ', err)

        try:
            result['artist_1']['image_url'] = result_search_artist_name['artists']['items'][1]['images'][1]['url']
            result['artist_1']['artist'] = result_search_artist_name['artists']['items'][1]['name']
            result['artist_1']['followers'] = result_search_artist_name['artists']['items'][1]['followers']['total']
            result['artist_1']['genres'] = result_search_artist_name['artists']['items'][1]['genres'][0]
            result['artist_1']['popularity']= result_search_artist_name['artists']['items'][1]['popularity']
        except IndexError as err:
            print('uups, we have a problem with your search, I dare you to try again (つ▀¯▀)つ: ', err)
        
        try:
            result['artist_2']['image_url'] = result_search_artist_name['artists']['items'][2]['images'][1]['url']
            result['artist_2']['artist'] = result_search_artist_name['artists']['items'][2]['name']
            result['artist_2']['followers'] = result_search_artist_name['artists']['items'][2]['followers']['total']
            result['artist_2']['genres'] = result_search_artist_name['artists']['items'][2]['genres'][0]
            result['artist_2']['popularity']= result_search_artist_name['artists']['items'][2]['popularity']
        except IndexError as err:
            print('uups, we have a problem with your search, I dare you to try again (つ▀¯▀)つ: ', err)

        try:
            result['artist_3']['image_url'] = result_search_artist_name['artists']['items'][3]['images'][1]['url']
            result['artist_3']['artist'] = result_search_artist_name['artists']['items'][3]['name']
            result['artist_3']['followers'] = result_search_artist_name['artists']['items'][3]['followers']['total']
            result['artist_3']['genres'] = result_search_artist_name['artists']['items'][3]['genres'][0]
            result['artist_3']['popularity']= result_search_artist_name['artists']['items'][3]['popularity']
        except IndexError as err:
            print('uups, we have a problem with your search, I dare you to try again (つ▀¯▀)つ: ', err)

        result_artists_json =json.dumps(result)
        return result_artists_json

    else:
        print(search.status_code)
        print('Request invalid')
    



def get_info_by_search_name(search_name, token):
    search_name = search_name.replace(' ', '+')
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': search_name, 'type':'track,artist,album', 'market':'MX', 'limit':1}
    header = {'Authorization': 'Bearer {}'.format(token)}
    search = requests.get(url_search, headers = header, params = search_params)

    if search.status_code == 200:
        result_search_name = search.json()

        result ={
                'track':{
                        'image_url':'none',
                        'title': 'none',
                        'artist': 'none', 
                        'album':'none', 
                        'duration':0
                        },
                'artist':{
                        'image_url': 'none',
                        'artist': 'none', 
                        'followers': 0, 
                        'genres':'none', 
                        'popularity':0
                        },
                'album':{
                        'image_url': 'none',
                        'name': 'none',
                        'artist': 'none',
                        'release_date': 'none'
                        }
                }

        
        result['track']['image_url'] = result_search_name['tracks']['items'][0]['album']['images'][1]['url']
        result['track']['title'] = result_search_name['tracks']['items'][0]['name']
        result['track']['artist'] = result_search_name['tracks']['items'][0]['artists'][0]['name']
        result['track']['album'] = result_search_name['tracks']['items'][0]['album']['name']
        duration_time = result_search_name['tracks']['items'][0]['duration_ms']
        result['track']['duration'] = time.strftime("%M:%S", time.gmtime(duration_time/1000))

        try:
            result['artist']['image_url'] = result_search_name['artists']['items'][0]['images'][1]['url']
            result['artist']['artist'] = result_search_name['artists']['items'][0]['name']
            result['artist']['followers'] = result_search_name['artists']['items'][0]['followers']['total']
            result['artist']['genres'] = result_search_name['artists']['items'][0]['genres'][0]
            result['artist']['popularity']= result_search_name['artists']['items'][0]['popularity']

        except IndexError as err:
            print('uups, we have a problem with your search, I dare you to try again (つ▀¯▀)つ: ', err)

        
        result['album']['image_url'] = result_search_name['albums']['items'][0]['images'][1]['url']
        result['album']['name'] = result_search_name['albums']['items'][0]['name']
        result['album']['artist'] = result_search_name['albums']['items'][0]['artists'][0]['name']
        result['album']['release_date']= result_search_name['albums']['items'][0]['release_date']


        result_name_json =json.dumps(result)
        return result_name_json

    else:
        print(search.status_code)
        print('Request invalid')

