from time import sleep
from selenium import webdriver
from .clear_cache import clear_firefox_cache

# Start a firefox driver (make sure that geckodriver is running first)
driver = webdriver.Firefox()

# Visit a website that places data in local storage
driver.get('http://127.0.0.1:5000')

# Stay at preferences page for 10 seconds to see the state
driver.get('about:preferences#privacy')
sleep(10)

# Clear the cache and hang around some more
clear_firefox_cache(driver)
sleep(10)

driver.quit()