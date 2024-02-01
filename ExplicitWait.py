

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
myexplicitwait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])

driver.get("https://www.google.com/")
element=driver.find_element(By.NAME,"q")
element.send_keys("selenium")
element.submit()
myresponse=myexplicitwait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
myresponse.click()
