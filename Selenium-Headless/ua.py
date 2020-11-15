import random
import logging


user_agents_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/2010010 1 Firefox/7.0.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb Kit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ( KHTML, like Gecko) Chrome/44.0.2403.157 Safari/53 7.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Geck o/20100101 Firefox/15.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100 101 Thunderbird/45.3.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.27 43.116 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko)'
]

def process_ua():
    try:
        user_agent = random.choice(user_agents_list)
        header = {'User-Agent':user_agent}
    except IndexError:
        logging.error("Couldn't fetch the user agent")
    return header