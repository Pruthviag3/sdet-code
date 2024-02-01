from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj=Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=ops)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# get column and row count

rowcount=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
colcount=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(rowcount)
print(colcount)

# print col and row values

# for r in range(2,rowcount+1):
#     for c in range(1,colcount+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="   ")
#     print()
#


# print particular author book and price name

for r in range(2, rowcount+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authorname== "Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(authorname,"   ",bookname,"   ",price)



