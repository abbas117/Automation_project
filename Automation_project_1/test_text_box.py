from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()

# text_field
text_field = driver.find_element(By.ID, "autocomplete")
text_field.send_keys("India")
print(text_field.get_attribute("value"))
time.sleep(2)