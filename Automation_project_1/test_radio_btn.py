from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()
time.sleep(1)

# radio_button
radio_btn = driver.find_elements(By.CLASS_NAME, "radioButton")
for radio in radio_btn:
    radio.click()
print("Clicked")


