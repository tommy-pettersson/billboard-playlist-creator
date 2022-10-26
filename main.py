from pprint import pprint
from networker import Networker
from webscraper import Webscraper

def main():

    print("Getting name of current user.")
    user_name = Networker.get_current_user()

    # print("Getting song titles.")
    # songs = Webscraper.get_song_names()

    # print("Getting spotify links.")
    # song_uris = [ Networker.get_song_uri(song) for song in songs ]

    print("Creating playlist.")
    playlist_id = Networker.create_playlist(user_name, "2002-10-01")
    print(playlist_id)


if __name__ == "__main__":
    main()