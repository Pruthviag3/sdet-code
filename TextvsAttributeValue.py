
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
element_email=driver.find_element(By.XPATH,"//input[@name='Email']")
element_email.clear()
element_email.send_keys("abc@gmail.com")
print("text",element_email.text)
print("attribute",element_email.get_attribute("value"))

element_login=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("text",element_login.text)
print("attribute",element_login.get_attribute("value"))
