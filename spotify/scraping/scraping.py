import requests

url_base = 'https://api.spotify.com/v1'

ep_artist = '/artists/{artist_id}'
id_zedd = '2qxJFvFYMEDqd7ui6kSAcq'
artist_id = id_zedd

#r = requests.get(url_base+ep_artist.format(artist_id = id_zedd))
#print(r.status_code)

def get_token():

    token_url = 'https://accounts.spotify.com/api/token'
    params = {'grant_type': 'client_credentials'}
    headers = {'Authorization': 'Basic ODAwMjM3YWRhMWI4NGUxYTlmNTU1YjY3OGIxZGM5Y2I6ZmQxNjA0Y2Q2YzM4NGIzYThlYzA4ZjI4ZDM0NzA2MWU'}
    r = requests.post(token_url, data = params, headers = headers )

    print(r.status_code)
    print(r.json())
    token = r.json()['access_token']
    return print(r.status_code)


def get_info_by_artist_id(artist_id, token):
    header = {'Authorization': 'Bearer {}'.format(token)}
    r = requests.get(url_base+ep_artist.format(artist_id = artist_id), headers = header)

    print(r.status_code)

    print(r.json())
    info_by_artist = r.json()

    return info_by_artist


def get_info_by_artist_name(artist_name):
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': artist_name, 'type':'artist', 'market':'MX'}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_artist_name = search.json()

    return result_search_artist_name


def get_info_by_album_name(album_name):
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': album_name, 'type':'album', 'market':'MX'}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_album_name = search.json()

    return result_search_album_name


def get_info_by_track_name(artist_name):
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': track_name, 'type':'track', 'market':'MX'}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_track_name = search.json()

    return result_search_track_name


def get_info_by_playlist_name(artist_name):
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': playlist_name, 'type':'playlist', 'market':'MX'}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_playlist_name = search.json()

    return result_search_playlist_name


def get_info_by_show_name(artist_name):
    url_search = 'https://api.spotify.com/v1/search'
    search_params = {'q': show_name, 'type':'show', 'market':'MX'}
    search = requests.get(url_search, headers = header, params = search_params)

    print(search.status_code)
    result_search_show_name = search.json()

    return result_search_show_name


def run():
    import requests
    url_base = 'https://api.spotify.com/v1'

    ep_artist = '/artists/{artist_id}'
    id_zedd = '2qxJFvFYMEDqd7ui6kSAcq'
    artist_id = id_zedd
    r = requests.get(url_base+ep_artist.format(artist_id = id_zedd))
    print(r.status_code)
    print('step1 ok')

"""     token_url = 'https://accounts.spotify.com/api/token'
    params = {'grant_type': 'client_credentials'}
    headers = {'Authorization': 'Basic ODAwMjM3YWRhMWI4NGUxYTlmNTU1YjY3OGIxZGM5Y2I6ZmQxNjA0Y2Q2YzM4NGIzYThlYzA4ZjI4ZDM0NzA2MWU'}
    r = requests.post(token_url, data = params, headers = headers )

    print(r.status_code)
    print(r.json())
    token = r.json()['access_token']

    print('step2 ok')

    header = {'Authorization': 'Bearer {}'.format(token)}
    r = requests.get(url_base+ep_artist.format(artist_id = artist_id), headers = header)

    print(r.status_code)

    print(r.json())
    info_by_artist = r.json()
 """


if '__name__' == '__main__':

    run()

