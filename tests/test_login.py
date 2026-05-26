from pages.login_page import LoginPage
import time


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    assert "inventory" in driver.current_url
