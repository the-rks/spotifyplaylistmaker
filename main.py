import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
SPOTIPY_CLIENT_ID = "f0a3099ca9a84a3fb39187237750d4ed"
SPOTIPY_CLIENT_SECRET = "cdcbd1ef8031430ba7cf655c4813c76d"
SPOTIPY_REDIRECT_URI='https://www.google.com/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])