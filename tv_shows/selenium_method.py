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


class TelevisionShows():  
        def main(self):
            ranks = []
            names = []
            years = []
            imdb_ratings = []
            links = [] 
            url = "https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&\
                    pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=ZE28XW126A1YYXS5FEBT&\
                    pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=tvmeter&ref_=chttvm_ql_6"
        
        
            options = Options()
            options.add_argument('-headless')
            driver = wb.Firefox(executable_path='/Users/geckodriver', options=options)
            # driver.maximize_window()
            driver.get(url)
            driver.implicitly_wait(3)

            text = driver.find_elements(By.CLASS_NAME, 'titleColumn')

            for prog in text:
                ranks.append(prog.text.split()[0])
                part2 = prog.text.split()[1:-1]
                names.append(delist(part2))
                years.append(prog.text.split()[-1])
                addr = prog.find_element(By.TAG_NAME, 'a').get_attribute('href')
                links.append(addr)

            imdb_rating = driver.find_elements(By.TAG_NAME, 'strong')
            for show in imdb_rating:
                rating = show.text 
                imdb_ratings.append(rating)
            
            content = {
                'ranks': ranks,
                'names': names,
                'years': years,
                'imdb_ratings': imdb_ratings,
                'links': links
            }

            driver.close()
            shows = pd.DataFrame(content)
            print(shows.head())
            print(shows.info())
            shows.to_csv('tv_sel.csv', index=False)

            shows = pd.read_csv('tv_sel.csv', dtype={'ranks':np.int32}, index_col='ranks', usecols=['ranks', 'names', 'years', 'imdb_ratings', 'links'])
            logging.info("finished reading the csv file")

            shows['years'] = shows['years'].str.replace('(', '').str.replace(')', '')

            shows.to_csv('tv_sel2.csv')

            shows = pd.read_csv('tv_sel2.csv',
                    dtype={'ranks':np.int64, 'years':np.int64}, 
                    index_col='ranks', 
                    usecols=['ranks', 'names', 'years', 'imdb_ratings', 'links'])

            print(shows.head())
            print(shows.info())



ff = TelevisionShows()
ff.main()