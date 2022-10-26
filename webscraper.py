import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

class Webscraper:

    def get_song_names(date):
        try:
            response = requests.get(url=f"{URL}{date}")
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            data = response.text

        soup = BeautifulSoup(data, "html.parser")
        songs = soup.find_all(name="ul", class_="o-chart-results-list-row")

        titles = [ song.h3.getText().strip() for song in songs ]
        return titles