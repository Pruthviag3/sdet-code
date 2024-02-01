import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()