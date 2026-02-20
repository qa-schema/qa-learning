from automation.pages.login_page import LoginPage
from automation.utils import save_screenshot


def test_invalid_password_shows_error(driver):
    try:
        page = LoginPage(driver).open()
        page.login("tomsmith", "wrong_password")

        assert "Your password is invalid!" in page.flash_text()
    except Exception:
        save_screenshot(driver, "test_invalid_password_shows_error")
        raise
