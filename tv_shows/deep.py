import pandas as pd 
import numpy as np

movie_page = pd.read_csv('movies.csv', index_col='rank')
pages = movie_page['link']
print(pages[:10])