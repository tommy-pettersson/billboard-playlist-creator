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
        else:
            return uri

    def create_playlist(user_name, date):
        playlist_name = f"{date} Billboard 100"

        try:
            response = sp.user_playlist_create(user=user_name, name=playlist_name, public=False, collaborative=False)
        except:
            print("Error creating playlist.")
        else:
            playlist_id = response["id"]
            return playlist_id

    def add_tracks_to_playlist(playlist_id, songs):
        try:
            sp.playlist_add_items(playlist_id, songs)
        except:
            print("Error adding tracks to playlist.")
        else:
            print("Succesfully added tracks to playlist.")
