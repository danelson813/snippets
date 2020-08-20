import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = ""  #Needs to be entered

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# out table is the last one on page
# getting the table head because it contains the col names
html_thead = soup.find_all('thead')[-1]

# getting all the rows in html_thead
html_tr = [tr for tr in html_thead.find_all('tr')]

# list to contain the table headings
headings = []

# loop through the table headings
for tr in html_tr:
    th = tr.find_all('th')
    # storing all th values in row and removing white space
    row = [i.text.strip() for i in th]
    headings.append(row)
print(headings)

# getting the table body
html_tbody = soup.find_all('tbody')[-1]
html_text = [tr for tr in html_tbody.find_all('tr')]
content = []

for tr in html_text:
    th = tr.find_all(['th', 'td'])
    row = [i.text.strip() for i in th]
    content.append(row)
print(content)

data = pd.DataFrame(content[:], columns=headings[0])

print(data.head())
print(data.describe())

print(data.info())

print(data.columns)

# rename column name if required
data = data.rename(columns={'First_column_name': 'New Name', 'Second Col_Name': 'New_name'})

#remove extra characters from columns
data['column_name'] = data['column_name'].str.replace('%', '')
data['column_name'] = data['column_name'].str.replace(',', '')