from pprint import pprint
from networker import Networker
from webscraper import Webscraper
import os

def main():

    os.system("cls" if os.name == "nt" else "clear")

    print("Welcome to the time-machine playlist creator.")

    chosen_date = input("Enter a date (YYYY-MM-DD): ")

    print("Getting name of current user.")
    user_name = Networker.get_current_user()

    print("Getting song titles.")
    songs = Webscraper.get_song_names(chosen_date)

    print("Getting Spotify links.")
    song_uris = [ Networker.get_song_uri(song) for song in songs ]

    print("Creating playlist.")
    playlist_id = Networker.create_playlist(user_name, chosen_date)

    print("Adding songs to your new playlist.")
    Networker.add_tracks_to_playlist(playlist_id, song_uris)

if __name__ == "__main__":
    main()