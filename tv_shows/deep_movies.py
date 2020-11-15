from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd 
import numpy as np
import time
from log_app import *
from selenium.common.exceptions import NoSuchElementException
logging.info('getting started')


def write_to_file(string):
    border = '\n*************************\n'
    with open('synopsis.txt', 'a') as f:
        f.write(string)
        f.write(border)



class MoviesSynopsis():  
        def main(self):
            logging.info('Getting started with main()')
            movies = pd.read_csv('movies.csv', index_col='rank')
            links = movies['link']
            synopsis_list = []
            start_urls = []
                           
            profile = wb.FirefoxProfile()
            profile.set_preference("general.useragent.override", 
            "[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36]")
            
            options = Options()
            options.add_argument('-headless')
            # driver = wb.Firefox(profile, executable_path='/Users/geckodriver', options=options )

            for i in range(1,251):    
                # driver.get(links[i])
                # driver.implicitly_wait(3)
                logging.info(f'index = {i}')

                try:
                    start_urls.append(links[i])
                    # driver.find_element_by_link_text('Plot Synopsis').click() 
                    # driver.implicitly_wait(3)              
                    # synopsis = driver.find_element(By.ID, 'plot-synopsis-content').text
                except NoSuchElementException as e:
                    # synopsis = 'No synopsis available'
                    # # logging.info('except: ', e)
                    # print('except: ', e)
                # finally:
                #     write_to_file(synopsis)
                #     synopsis_list.append(synopsis)

                # time.sleep(5)

            driver.close()
         

ff = MoviesSynopsis()
ff.main()
