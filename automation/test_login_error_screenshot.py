import pytest
pytestmark = pytest.mark.ui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login_shows_error_and_screenshot():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 10)

        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys("wrong_user")
        password_input.send_keys("wrong_password")
        password_input.send_keys(Keys.RETURN)

        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )

        assert "invalid" in error_message.text.lower()

    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        raise e

    finally:
        driver.quit()
