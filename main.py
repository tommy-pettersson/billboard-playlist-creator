from pprint import pprint
from networker import Networker
from webscraper import Webscraper

def main():
    # print("Getting song titles.")
    # songs = Webscraper.get_song_names()

    # print("Getting spotify links.")
    # song_uris = [ Networker.get_song_uri(song) for song in songs ]

    print(Networker.get_current_user())

if __name__ == "__main__":
    main()