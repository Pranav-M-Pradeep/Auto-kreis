from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (Ensure chromedriver.exe is in the same folder or set PATH)
driver = webdriver.Chrome()

# Open the webpage
driver.get("http://localhost/Car/reg.html")  # Change this to your actual file or hosted link
driver.maximize_window()

# Switch to Signup form
driver.find_element(By.ID, "go-to-signup").click()
time.sleep(1)  # Wait for the form to switch

# Fill in the form fields
driver.find_element(By.ID, "signup-name").send_keys("John Doe")
driver.find_element(By.ID, "signup-email").send_keys("john.doe@example.com")
driver.find_element(By.ID, "signup-phone").send_keys("9876543210")
driver.find_element(By.ID, "signup-vehicle").send_keys("Tesla Model X")
driver.find_element(By.ID, "signup-password").send_keys("StrongPass123")

# Click the Sign Up button
driver.find_element(By.CSS_SELECTOR, ".auth-btn").click()

# Wait and check for success message or redirection (Modify as needed)
time.sleep(2)

# Validation - Check if form submits successfully
if "Thank you" in driver.page_source or "Success" in driver.page_source:
    print("Signup Test Passed ✅")
else:
    print("Signup Test Failed ❌")

# Close the browser
driver.quit()
