from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  
driver = webdriver.Chrome()
driver.get("file:///C:/xampp/htdocs/Car/booking.html")
user_id_field = driver.find_element(By.NAME, "user_id")
for char in "12345":
    user_id_field.send_keys(char)
    time.sleep(0.5) 
date_field = driver.find_element(By.NAME, "date")
date_field.send_keys("02-23-2015")  
driver.execute_script("document.getElementById('service-time').value = '10:00';")
time.sleep(0.5)
notes_field = driver.find_element(By.NAME, "notes")
for char in "Please check tire pressure too.":
    notes_field.send_keys(char)
    time.sleep(0.2)
driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]").click()
time.sleep(2)
if "file:///C:/xampp/htdocs/Car/payment.html" in driver.current_url:
    print(" Test Passed: Successfully navigated to the payment page.")
else:
    print("Test Failed: Did not navigate, likely due to validation failure.")
driver.quit()
