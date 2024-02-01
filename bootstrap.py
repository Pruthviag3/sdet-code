import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


serv_obj=Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@aria-label='Country']").click()
countrylists=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li")
for country in countrylists:
    if country.text=="Albania":
        country.click()
        time.sleep(5)
        driver.save_screenshot(os.getcwd()+"\\Homepage.png")
        driver.get_screenshot_as_png()
        break



