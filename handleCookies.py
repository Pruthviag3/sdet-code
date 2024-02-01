import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import os


serv_obj=Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies=driver.get_cookies()
print("All cookies:",len(cookies))

# for c in cookies:
#     print(c)

driver.add_cookie({"name":"abc", "value":"xyz"})
cookies=driver.get_cookies()
print("All cookies:",len(cookies))

driver.delete_cookie("abc")
cookies=driver.get_cookies()
print("All cookies:",len(cookies))
