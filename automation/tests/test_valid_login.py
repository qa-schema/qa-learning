from automation.pages.login_page import LoginPage
from automation.pages.secure_page import SecurePage
from automation.utils import save_screenshot


def test_valid_login_redirects(driver):
    try:
        page = LoginPage(driver).open()
        page.login("tomsmith", "SuperSecretPassword!")

        SecurePage(driver).wait_loaded()
        assert "/secure" in driver.current_url
    except Exception:
        save_screenshot(driver, "test_valid_login_redirects")
        raise
