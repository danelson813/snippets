from time import sleep
from webdriver_setup import get_webdriver_for
from selenium.webdriver import FirefoxOptions, FirefoxProfile
from fake_useragent import UserAgent

useragent = UserAgent()
firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")
profile = FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
driver = get_webdriver_for("firefox", options=firefox_options, firefox_profile=profile)


# start the browser with the given url
url = "https://books.toscrape.com"
driver.get(url)

# print the title of the website
print(f"Title: {driver.title}")

# sleep 5 seconds
sleep(5)

# quit browser
driver.quit()
