from pprint import pprint
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy

load_dotenv()

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

class Networker:

    def get_song_uri(song_name):
        try:
            response = sp.search(q=song_name)
            uri = response["tracks"]["items"][0]["uri"]
        except:
            print("Song not found.")
            pass
        else:
            return uri

