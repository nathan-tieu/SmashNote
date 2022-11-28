import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

creds = sp.oauth2.SpotifyClientCredentials(
    client_id='26c9c4896ef94f90b14eece3ae4f6d2e', client_secret='4f4a5ae2a1174440808403b7b0f26ba4')
client = sp.client.Spotify(client_credentials_manager=creds)
genres = ['k-pop']
recomendations = client.recommendations(
    seed_genres=genres, target_energy=0.99, target_liveness=0.99, target_danceability=0.99, limit=1)
song_data = list()
print(recomendations['tracks'])
for song in recomendations['tracks']:
    song_data.append(client.track(track_id=song['id']))
# print(song_data)