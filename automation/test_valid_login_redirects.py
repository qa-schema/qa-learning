from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login_redirects_to_inventory():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    WebDriverWait(driver, 10) .until(
        EC.url_contains("inventory")
    )
    assert "inventory" in driver.current_url

    driver.quit()