from automation.utils import save_screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_invalid_password_shows_error():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)

        flash = driver.find_element(By.ID, "flash").text

        assert "Your password is invalid!" in flash

    except Exception:
        save_screenshot(driver, "test_invalid_passwoord_shows_error")
        raise

    finally:
        driver.quit()




