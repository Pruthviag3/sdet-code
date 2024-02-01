import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")
driver.back()
driver.forward()
driver.refresh()
time.sleep(4)

driver.quit()
