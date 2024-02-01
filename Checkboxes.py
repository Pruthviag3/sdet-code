import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# 1.select one checkbox
# driver.find_element(By.XPATH,"//input[@value='Cricket']").click()
# time.sleep(5)
#2.select all checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkbox')]")
print(len(checkboxes))
#Approach 1
# for i in range (len(checkboxes)):
#     checkboxes[i].click()

#Approach 2
for checkbox in checkboxes:
    checkbox.click()

#3.Select checkboxes with condition
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('value')
#     if weekname =='Cricket' or weekname =='Hockey':
#         checkbox.click()

#4.Select last two check boxes
# for i in range(len(checkboxes)-1,len(checkboxes)):
#     checkboxes[i].click()
#     time.sleep(5)
#5.Select first two check boxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

#6.Uncheck all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
        time.sleep(4)
