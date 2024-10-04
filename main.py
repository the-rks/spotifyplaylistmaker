import requests

# Replace these variables with your credentials and tokens
access_token = 'BQDPLkPUSstN-omrzzpWtekUq6ExEO1fBgqKzq4NH7bsazxhKg24z__NLxHJW_sc85OLSyIoX6GMEaIS2sJHi-hdrbJycBemFm4lJ-RJhfZSGw1o69WV6hykeK9Z65qXmy9ubihqRtbtA0jRbagu9_497tI-UvEhkaylNVnMnR7Dvhvdodn4Fd5KHN_4aRfXdzHhyXUHH7UUE6b-nX8Zd3bQzWf_heewh1eQtFes2pL9w9rSDx1CebpITwpR89Tao42UGIa4c31LlQreZ9Yv1MyLU5eOgg0t'

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