from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()  
driver.get("file:///C:/xampp/htdocs/Car/car_service.html")  
original_window = driver.current_window_handle
wait = WebDriverWait(driver, 10)
menu_links = {
    "Home": "//a[@href='service_list.html']",
    "SignUp/Login": "//a[@href='http://localhost/Car/reg.html']",
    "Services": "//a[@href='service_list.html']",
    "Booking": "//a[@href='booking.html']",
    "Profile": "//a[@href='service_list.html']",
    "Help Us": "//a[@href='service_list.html']"
}
for name, xpath in menu_links.items():
    try:
        link = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        link.click()
        print(f"Clicked '{name}', Current URL: {driver.current_url}")
        wait.until(lambda d: d.current_url != "file:///C:/xampp/htdocs/Car/car_service.html")
        driver.back()
        wait.until(lambda d: d.current_url == "file:///C:/xampp/htdocs/Car/car_service.html")
    except Exception as e:
        print(f"Error with '{name}': {e}")
driver.quit()
