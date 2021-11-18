import requests
import os

auth_url = 'https://accounts.spotify.com/api/token'
base_url = 'https://api.spotify.com/v1/'

client_id = os.getenv('Client_ID')
client_secret = os.getenv('Client_Secret')

def get_access_token():
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token

def find(query):
    access_token = get_access_token()
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    response = {'artist': None, 'album': None, 'track': None, 'playlist': None}
    response['artist'] = requests.get( base_url + f'search?q={query}&type=artist', headers=headers).json()
    response['album'] = requests.get( base_url + f'search?q={query}&type=album', headers=headers).json()
    response['track'] = requests.get( base_url + f'search?q={query}&type=track', headers=headers).json()
    response['playlist'] = requests.get( base_url + f'search?q={query}&type=playlist', headers=headers).json()
    return response