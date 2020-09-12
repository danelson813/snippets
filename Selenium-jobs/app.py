from selenium.webdriver.common.by import By  
from time import sleep  
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC#specify driver path    
DRIVER_PATH = '/Users/chromedriver'    
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

driver.get('https://indeed.com')

initial_search_button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
initial_search_button.click()



advanced_search = driver.find_element_by_xpath("//a[contains(text(),'Advanced Job Search')]")
advanced_search.click()
sleep(1)
#search data science     
search_job = driver.find_element_by_id("as_and")    
search_job.send_keys(['data science'])

# where
where = driver.find_element_by_id('where')
where.clear()
where.send_keys(['Seattle, WA'])

#set display limit of 30 results per page    
display_limit = driver.find_element_by_xpath('//select[@id="limit"]//option[@value="30"]')    
display_limit.click()

#sort by date    
sort_option = driver.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]')    
sort_option.click()

search_button = driver.find_element_by_xpath('//*[@id="fj"]')    
search_button.click()

sleep(2)

close_popup = driver.find_element_by_xpath("//a[@class='icl-CloseButton popover-x-button-close']") 
close_popup.click()

jobs = driver.find_elements_by_class_name('jobsearch-SerpJobCard unifiedRow row result clickcard vjs-highlight')

for job in jobs:
    link = job.find_element_by_xpath('.//h2/a').get_attribute('href')
    print(link)
    title = job.find_element_by_xpath('.//h2/a').text
    print(title)
    location = job.find_element_by_xpath(".//span[@class='location accessible-contrast-color-location']").text 
    print(location)
    print('*'*45)

driver.close()