
import logging

logging.basicConfig(
    filename='logfile.log',
    filemode='a',
    level=logging.DEBUG,
    format=f'%(levelname)s → %(asctime)s → %(message)s',
    datefmt="%Y/%m/%d %H:%M:%S"
)

