
import logging

logging.basicConfig(
    filename='logfile.log',
    filemode='w',
    level=logging.INFO,
    format=f'%(levelname)s → %(asctime)s → %(message)s',
    datefmt="%Y/%m/%d %H:%M:%S"
)

