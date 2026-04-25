import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_invalid_login_shows_error_and_screenshot():
    from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
    driver.get("https://example.com/login")  # TODO: echte Seite einsetzen

    try:
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys("wrong_user")
        password_input.send_keys("wrong_password")
        password_input.send_keys(Keys.RETURN)

        time.sleep(2)

        error_message = driver.find_element(By.ID, "error")

        assert "invalid" in error_message.text.lower()

    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        raise e

    finally:
        driver.quit()
