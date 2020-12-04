from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import shutil

html_page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(html_page.content, 'html.parser')
warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling

images = book_container.findAll('img')
for i in range(len(images)):
    example = images[i]
    title = example.attrs['alt'].replace(' ', '_')
    url_base = "http://books.toscrape.com/" #Original website
    url_ext = example.attrs['src'] #The extension you pulled earlier
    full_url = url_base + url_ext #Combining first 2 variables to create       a complete URL
    r = requests.get(full_url, stream=True) #Get request on full_url
    if r.status_code == 200:                     #200 status code = OK
        with open(f"images/{title}.jpg", 'wb') as f: 
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


    # img = mpim.imread(f'images/{title}.jpg')
    # imgplot = plt.imshow(img)
    # plt.show()