from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)

#new_window
new_window = driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print("new window title is: ", driver.title)

contact_us = driver.find_element(By.XPATH, "(//a[@href='contactus.html'])[1]").click()
driver.maximize_window()
time.sleep(1)

driver.close()
driver.switch_to.window(windows[0])
print("back to orignal")
time.sleep(1)

#new_tab
new_tab = driver.find_element(By.XPATH,"//a[@class = 'btn-style class1 class2']").click()
wait = WebDriverWait(driver , 5)
tab = driver.window_handles
driver.switch_to.window(tab[1])
print("New tab title:", driver.title)


wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='nav-item']//a[normalize-space()='Courses']")))
course = driver.find_element(By.XPATH, "//li[@class='nav-item']//a[normalize-space()='Courses']").click()
driver.maximize_window()
time.sleep(2)
driver.close()

driver.switch_to.window(windows[0])
print("back to orignal")
time.sleep(2)

