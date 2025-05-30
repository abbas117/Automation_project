from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 1400);")
time.sleep(2)

print("The title of this website: " , driver.title)

iframe = driver.find_element(By.ID, "courses-iframe")
driver.switch_to.frame(iframe)
all_access_plan = driver.find_element(By.XPATH, "//a[@class='new-navbar-highlighter' and contains(text(),'All Access plan')]").click()
time.sleep(2)
print()
driver.switch_to.default_content()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);")
footer = driver.find_element(By.ID,"gf-BIG")
print(footer.text)
