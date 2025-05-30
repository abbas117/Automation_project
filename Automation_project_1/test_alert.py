from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 
driver.maximize_window()

text_box = driver.find_element(By.XPATH, '//input[@name = "enter-name"]').send_keys("Muttaqui Abbas")
time.sleep(2)

#alert_button
alert_button = driver.find_element(By.ID, 'alertbtn').click()
time.sleep(2)
alert = driver.switch_to.alert
print("alert message is: ", alert.text)
alert.accept()

confirm_btn = driver.find_element(By.ID, 'confirmbtn').click()
time.sleep(2)
alert = driver.switch_to.alert
print("confirm message is: ", alert.text)
alert.dismiss()

# table = driver.find_element(By.XPATH, "(//table[@id='product'])[1]")
# print(table.text)# print(table.text)



driver.quit()