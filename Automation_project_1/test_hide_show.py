from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 200);")

text_box = driver.find_element(By.ID, "displayed-text")
hide_button = driver.find_element(By.ID, "hide-textbox")
show_button = driver.find_element(By.ID, "show-textbox")

assert text_box.is_displayed() == True
print("text box is displayed")

hide_button.click()    
time.sleep(2)
assert text_box.is_displayed() == False 
print("clicked on hide button but text box is still displayed")

show_button.click()
time.sleep(2)
assert show_button.is_displayed() == True
print("clicked on show button and text box is displayed")