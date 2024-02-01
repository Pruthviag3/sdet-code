import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/register")
print(driver.find_element(By.XPATH, "//input[@name='FirstName']").is_enabled())
print(driver.find_element(By.XPATH, "//input[@name='FirstName']").is_displayed())

radio_button =driver.find_element(By.XPATH,"//input[@value='M']")
radio_button.click()
print(radio_button.is_selected())
driver.find_element(By.XPATH, "//input[@name='FirstName']").send_keys("Hello")
driver.find_element(By.XPATH,"//input[@name='LastName']").send_keys("Hi")
driver.find_element(By.XPATH,"//input[@name='Email']").send_keys("Hi@gmail.com")
driver.find_element(By.XPATH,"//input[@name='Company']").send_keys("Amazon")

driver.find_element(By.XPATH,"//input[@name='Password']").send_keys("Abcd@123")
driver.find_element(By.XPATH,"//input[@name='ConfirmPassword']").send_keys("Abcd@123")
time.sleep(4)
driver.find_element(By.XPATH,"//a[normalize-space()='Facebook']").click()

driver.quit()


