from pprint import pprint
import requests
from bs4 import BeautifulSoup
from networker import Networker

URL = "https://www.billboard.com/charts/hot-100/2002-08-17/"

try:
    response = requests.get(url=URL)
    response.raise_for_status()
except requests.HTTPError as e:
    print(e)
else:
    data = response.text

soup = BeautifulSoup(data, "html.parser")
songs = soup.find_all(name="ul", class_="o-chart-results-list-row")

titles = [ song.h3.getText().strip() for song in songs ]
artists = [ song.find_all(name="span", class_="c-label")[1].getText().strip() for song in songs ]

song_uris = [ Networker.get_song_uri(title) for title in titles ]
print(len(song_uris))