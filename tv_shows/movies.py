from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd 
import numpy as np
from log_app import *
# import time


def delist(list):
        result = ''
        for i in range(len(list)):    
            result += list[i] + " "
        return str(result)


class TopMovies():  
        def main(self):
            logging.info('Getting started')
            ranks = []
            names = []
            years = []
            links = [] 
            url = "https://www.imdb.com/chart/top-english-movies?\
                pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-\
                f0efa18182cd&pf_rd_r=3NB323VG851RV8M7H5YH&pf_rd_s=right-4&pf_rd_t=\
                15506&pf_rd_i=top&ref_=chttp_ql_4"
            # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
            profile = wb.FirefoxProfile()
            profile.set_preference("general.useragent.override", 
            "[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36]")
        

            options = Options()
            options.add_argument('-headless')
            driver = wb.Firefox(profile, executable_path='/Users/geckodriver', options=options )
            
            driver.get(url)
            driver.implicitly_wait(3)
            print('got here')
            results = driver.find_elements(By.CLASS_NAME, 'titleColumn')
            for result in results:
                rank = int(result.text.split()[0].replace('.', ''))
                name = delist(result.text.split()[1:-1])
                year = int(result.text.split()[-1].replace('(', '').replace(')', ''))
                link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
                ranks.append(rank)
                names.append(name)
                years.append(year)
                links.append(link)
                
            driver.close()
            content = {
                'rank': ranks,
                'name': names,
                'year': years,
                'link': links
            }

            movies = pd.DataFrame(content)
            print(movies.head())
            print(movies.info())
            movies.to_csv('movies.csv', index=False)
            
            movies = pd.read_csv('movies.csv', index_col='rank')
            print(movies.head())
            print(movies.info())
            movies.to_csv("movies_final.csv")

ff = TopMovies()
ff.main()