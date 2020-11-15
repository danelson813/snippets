from datetime import datetime
import logging

logging.basicConfig(
    filename='test.log',
    filemode='a',
    level=logging.DEBUG,
    format=f'%(levelname)s → {datetime.now()} → %(name)s:%(message)s')