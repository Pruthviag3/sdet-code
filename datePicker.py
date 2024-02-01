import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=ops)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("03/03/2024")
# time.sleep(5)

date="03"
month="March"
year="2024"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

    dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

    for ele in dates:
        if ele.text==date:
            ele.click()
            time.sleep(5)
            break









