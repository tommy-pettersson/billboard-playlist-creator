from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy

load_dotenv()

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

class Networker:

    def get_current_user():
        try:
            response = sp.current_user()
        except:
            print("Error getting user data.")
        else:
            user_name = response["display_name"]
            return user_name

    def get_song_uri(song_name):
        try:
            response = sp.search(q=song_name)
            uri = response["tracks"]["items"][0]["uri"]
        except:
            print("Song not found.")
            pass
        else:
            return uri

