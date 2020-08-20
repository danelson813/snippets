
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


headless_options = Options()
headless_options.add_argument('--headless')

driver = webdriver.Chrome(options=headless_options)
driver.get('https://www.bbc.co.uk/news')

search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="orb-search-q"]')))
#search_box = driver.find_element_by_css_selector('input[id="orb-search-q"]')


ActionChains(driver).move_to_element(search_box).click() \
	.send_keys('Global coronavirus updates').key_down(Keys.ENTER).perform()

top_titles = driver.find_elements_by_css_selector('div[class="css-14rwwjy-Promo ett16tt11"]')

with open('Coronavirus_headlines.txt', 'w') as cor_virus:
	for title in top_titles:
		headline = title.find_element_by_css_selector('p[class="css-1aofmbn-PromoHeadline ett16tt4"]').text
		cor_virus.write('\n')
		cor_virus.write(headline)
		print(headline)