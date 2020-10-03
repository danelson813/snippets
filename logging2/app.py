
import logging

logging.basicConfig(
    filename='logs/logfile.log',
    filemode='a',
    level=logging.DEBUG,
    format=f'%(levelname)s → %(asctime)s → %(message)s',
    datefmt="%Y/%m/%d %H:%M:%S"
)

logging.info('Info')
logging.debug('Debug')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')
logging.warning('WARNING')
