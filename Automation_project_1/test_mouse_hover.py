from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollBy(0,900);")
time.sleep(2)
mouse_hover = driver.find_element(By.ID, "mousehover")
action = ActionChains(driver)
action.move_to_element(mouse_hover).perform()

driver.find_element(By.XPATH, "//a[text()='Reload']").click()
time.sleep(2)


