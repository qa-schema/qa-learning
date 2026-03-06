from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_username():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
        )
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("wronguser")
        password.send_keys("SuperSecretPassword!")
        login_button.click()

        error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "Your username is invalid!" in error_message.text

    finally:
        driver.quit()
