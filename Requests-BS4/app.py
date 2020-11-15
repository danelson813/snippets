# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://yelp.com"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())
