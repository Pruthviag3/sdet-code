import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import os


serv_obj=Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()


# reglink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
# time.sleep(10)

# in selenium 4
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.amazon.com")

driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.amazon.com")
