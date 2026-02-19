from automation.utils import save_screenshot

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_password_shows_error(driver):
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("wrongpassword")

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        flash_text = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
        assert "Your password is invalid!" in flash_text

    except Exception:
        save_screenshot(driver, "test_invalid_password_shows_error")
        raise




