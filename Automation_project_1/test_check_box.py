from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()

# check_box
check_boxs = driver.find_elements(By.XPATH,"//input[@type = 'checkbox']")

for check_box in check_boxs:
    if check_box == check_boxs[1]:
        pass
    else:
        check_box.click()
print(len(check_boxs))
time.sleep(1)
