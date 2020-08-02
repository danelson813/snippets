'''
    Uses selenium firefox headlessly to connect to a url and download
    the page source.  One can add a headers section to rotate the 
    user-agent for each request. 
'''
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By


if __name__ == "__main__":
    options = Options()
    options.add_argument('-headless')
    driver = Firefox( options=options)
    driver.get('http://www.google.com')
    print(driver.page_source)
    driver.quit()