from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

import pytest

@pytest.fixture()
def driver():

    service = Service(
        executable_path=ChromeDriverManager().install()
    )

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    driver.quit()

@pytest.fixture
def logged_in_inventory(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login_as_standard_user()

    return inventory