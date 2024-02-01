import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='Skills']"))
# drpcountry.select_by_visible_text("Adobe Photoshop")
# drpcountry.select_by_value("Analytics")
# drpcountry.select_by_index(4)
# time.sleep(5)

alloptions=drpcountry.options
print(len(alloptions))
#
# for opt in alloptions:
#     print(opt.text)

for opt in alloptions:
    if opt.text=="Analytics":
        opt.click()
        break



