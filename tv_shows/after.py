import pandas as pd 
import numpy as np
from log_app import *

shows = pd.read_csv('tv_shows.csv', dtype={'ranks':np.int32}, index_col='ranks', usecols=['ranks', 'titles', 'years', 'imdb_ratings', 'links'])
logging.info("finished reading the csv file")


shows['years'] = shows['years'].str.replace('(', '').str.replace(')', '')

shows.to_csv('tv_shows2.csv')

shows = pd.read_csv('tv_shows2.csv',
                    dtype={'ranks':np.int64, 'years':np.int64}, 
                    index_col='ranks', 
                    usecols=['ranks', 'titles', 'years', 'imdb_ratings', 'links'])

print(shows.head())
print(shows.info())