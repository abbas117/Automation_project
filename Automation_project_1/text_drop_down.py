from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.support.ui import Select


driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()

# drop_down
drop_down = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
drop_down.select_by_value("option1")
drop_down.select_by_index(2)
drop_down.select_by_index(3)
time.sleep(2)