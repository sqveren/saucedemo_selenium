from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

import pytest

@pytest.fixture()
def driver():

    service = Service(
        executable_path=ChromeDriverManager().install()
    )

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

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

@pytest.fixture
def logged_and_checkout_page(driver, logged_in_inventory):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    logged_in_inventory.add_to_cart_by_name(
        "sauce-labs-bike-light"
    )

    logged_in_inventory.open_cart()
    cart_page.go_to_checkout()

    return checkout_page