
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# driver=webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/register")
# single element
# element=driver.find_element(By.XPATH,"//input[@placeholder='Search store']")
# element.send_keys("vivo")

# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)

# element=driver.find_element(By.LINK_TEXT,"Log")
# element.click()

# multiple elements

# elements=driver.find_elements(By.XPATH,"//input[@placeholder='Search store']")
# print(len(elements))
# elements[0].send_keys("vivo")

# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
# print(elements[0].text)
# for ele in elements:
#     print(ele.text)

elements=driver.find_elements(By.LINK_TEXT,"Log")
print(len(elements))


driver.quit()








