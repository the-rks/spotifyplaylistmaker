import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
SPOTIPY_CLIENT_ID = "f0a3099ca9a84a3fb39187237750d4ed"
SPOTIPY_CLIENT_SECRET = "cdcbd1ef8031430ba7cf655c4813c76d"
SPOTIPY_REDIRECT_URI = 'https://www.google.com/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
headers = [] #get the songs later
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

response = requests.get('https://api.spotify.com/v1/me/tracks', headers=headers)

if response.status_code == 200:
    liked_songs = response.json()
    for item in liked_songs['items']:
        track = item['track']
        print(f"{track['name']} by {track['artists'][0]['name']}")
else:
    print(f"Error: {response.status_code}")

# comment! 

#another comment yey 
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])
