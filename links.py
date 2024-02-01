import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver.get("http://www.deadlinkcity.com/")
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

links=driver.find_elements(By.XPATH,"//a")
print(len(links))

count=0
for link in links:
    url=link.get_attribute('href')
    try:
     response=requests.head(url)
    except:
     None

    if response.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is normal link")


print("number of broken link",count)
