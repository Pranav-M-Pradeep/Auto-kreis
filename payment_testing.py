from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("file:///C:/xampp/htdocs/Car/payment.html")  
driver.maximize_window()
def switch_tab(tab_name):
    tab_button = driver.find_element(By.XPATH, f"//button[@data-target='{tab_name}']")
    tab_button.click()
    time.sleep(1)  
print("Testing QR Code Payment...")
switch_tab("qr")
qr_text = driver.find_element(By.XPATH, "//div[@id='qr']/p").text
assert "Scan the QR code to pay" in qr_text, "QR Code text not found!"
print("*** QR Code Test Passed***")
print("Testing Card Payment...")
switch_tab("card")
card_number = driver.find_element(By.ID, "cardNumber")
card_number.send_keys("12345678")
time.sleep(1)
error_message = driver.find_element(By.ID, "cardError").is_displayed()
assert error_message, "Card validation failed!"
print("*** Card Validation Error Displayed***")
card_number.clear()
card_number.send_keys("4111111111111111")  
driver.find_element(By.XPATH, "//input[@placeholder='Card Holder Name']").send_keys("John Doe")
driver.find_element(By.ID, "expiryDate").send_keys("12/25")
driver.find_element(By.ID, "cvv").send_keys("123")
pay_button = driver.find_element(By.XPATH, "//div[@id='card']//button[contains(text(),'Pay Now')]")
pay_button.click()
time.sleep(1)
print("***Card Payment Test Passed***")
print("Testing UPI Payment...")
switch_tab("upi")
upi_input = driver.find_element(By.ID, "upiID")
upi_input.send_keys("invalidupi")
time.sleep(1)
upi_error = driver.find_element(By.ID, "upiError").is_displayed()
assert upi_error, "UPI validation failed!"
print("***UPI Validation Error Displayed***")
upi_input.clear()
upi_input.send_keys("test@upi")
upi_pay_button = driver.find_element(By.XPATH, "//div[@id='upi']//button[contains(text(),'Pay via UPI')]")
upi_pay_button.click()
time.sleep(1)
print("***UPI Payment Test Passed***")
driver.quit()
