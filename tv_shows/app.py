import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 
from log_app import *

headers = {"User-Agent": "Mozilla/5.0"}
url =   "https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&\
        pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=ZE28XW126A1YYXS5FEBT&\
        pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=tvmeter&ref_=chttvm_ql_6"

base_url = 'https://www.imdb.com'

response = requests.get(url, headers=headers)

soup = bs(response.content, 'lxml')
logging.info("Soup established")

ranks = []
names = []
years = []
imdb_ratings = []
links = []

shows = soup.find('tbody', class_='lister-list').find_all('tr')
for show in shows:
    title = show.find('td', class_='titleColumn').text.split('\n')

    rank = title[1].strip()
    ranks.append(rank)

    name = title[2].strip().replace(',', '-')
    names.append(name)

    year = title[3]
    years.append(year)

    link = base_url + show.find('td', class_='titleColumn').find('a')['href']
    links.append(link)

    imdb_rating = show.find('td', class_='ratingColumn imdbRating').text.strip()
    imdb_ratings.append(imdb_rating)

content = {
    'ranks': ranks,
    'titles': names,
    'years': years,
    'imdb_ratings': imdb_ratings,
    'links': links
}

tv_shows = pd.DataFrame(content)
print(tv_shows.head())
print(tv_shows.info())
tv_shows.to_csv('tv_shows.csv')