import requests

# Replace these variables with your credentials and tokens
access_token = 'YOUR_ACCESS_TOKEN'

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get('https://api.spotify.com/v1/me/tracks', headers=headers)

if response.status_code == 200:
    liked_songs = response.json()
    for item in liked_songs['items']:
        track = item['track']
        print(f"{track['name']} by {track['artists'][0]['name']}")
else:
    print(f"Error: {response.status_code}")

# comment! 