from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


import time

# Initialize the Chrome driver (change to GeckoDriverManager() for Firefox)
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://example.com/login")

    # Find the username field and enter the username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("your_username")

    # Find the password field and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("your_password")

    # Find the login button and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for the next page to load
    time.sleep(20)  # Adjust the sleep time as needed

    # Optionally, you can now perform further actions on the logged-in page
    # Example: Print the title of the logged-in page
    print(driver.title)

finally:
    # Close the browser
    driver.quit()
