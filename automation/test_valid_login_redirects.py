from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login_redirects_to_inventory(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    wait.until(EC.url_contains("/secure"))

    assert "/secure" in driver.current_url
