import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.goibibo.com/flights/")
driver.maximize_window()
# main_page=driver.current_window_handle
driver.implicitly_wait(20)
# driver.find_element(By.XPATH,"//body//div//p[4]").click()
# time.sleep(5)
# for handle in driver.window_handles:
#     if handle != main_page:
#         print(handle)
# #         Login_Signup = handle
# #
# # driver.switch_to.window(Login_Signup)
# driver.find_element(By.XPATH,"//input[@name='phone']").send_keys("9876543021")
# time.sleep(5)
# continue_button=driver.find_element(By.XPATH,"//button[normalize-space()='Continue']")
# continue_button.is_enabled()
# continue_button.click()

driver.find_element(By.XPATH,"//span[@role='presentation']").click()
driver.find_element(By.XPATH,"//p[normalize-space()='Flights']").click()
driver.find_element(By.XPATH,"(//div[@class='sc-12foipm-16 wRKJm fswFld '])[1]").click()
# from_point.click()
# # # time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Bang")
list_from_elements=driver.find_elements(By.XPATH,"//ul[@id='autoSuggest-list']//li")
for list in list_from_elements:
    print(list.text)
    if "Bengaluru" in list.text:
        list.click()
        break
to_element=driver.find_element(By.XPATH,"//div[@class='sc-12foipm-38 dAUhfz']")
to_element.click()
# to_element.send_keys("Dub")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Dub")
list_to_elements=driver.find_elements(By.XPATH,"//ul[@id='autoSuggest-list']//li")
for li in list_to_elements:
    print(li.text)
    if "Dubai" in li.text:
        li.click()
        break
driver.find_element(By.XPATH,"(//div[@class='sc-12foipm-34 iHoHRr'])[3]").click()

driver.find_element(By.XPATH,"//div[@aria-label='Thu Nov 23 2023']//p[@class='fsw__date'][normalize-space()='23']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Done']").click()
driver.find_element(By.XPATH,"//span[@class='sc-12foipm-85 fUaVPB']").click()



