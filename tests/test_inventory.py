from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import time

def test_update_checkout_badge(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    #додавання айтему в кошик
    inventory_page.add_to_cart_by_name("sauce-labs-bike-light")

    #перевірка справності віджета біля іконки
    assert inventory_page.get_num_of_items_in_cart() == 1


def test_update_checkout_badge(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    #додавання айтему в кошик
    inventory_page.add_to_cart_by_name("sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart_by_name("sauce-labs-bike-light")

    #перевірка справності віджета біля іконки
    assert inventory_page.get_num_of_items_in_cart() == 2

def test_inventory_contains_items(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    # перевірка справності віджета біля іконки
    assert inventory_page.get_items_count() > 0

def test_sort_by_high_to_low(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    before = inventory_page.get_item_prices()
    #Дія
    inventory_page.sort_by("Price (low to high)")

    after = inventory_page.get_item_prices()
    assert after == sorted(before)

def test_sort_by_high_to_low(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    before = inventory_page.get_item_prices()
    #Дія
    inventory_page.sort_by("Price (high to low)")

    after = inventory_page.get_item_prices()
    assert after == sorted(before, reverse=True)

def test_add_item_go_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    inventory_page.add_item_open_cart("sauce-labs-bolt-t-shirt")
    #assert "Sauce Labs Bolt T-Shirt" in cart_page.get_cart_item_names()

def test_remove_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()


    inventory_page.add_to_cart_by_name("sauce-labs-bolt-t-shirt")
    assert inventory_page.get_num_of_items_in_cart() == 1

    inventory_page.remove_from_cart("sauce-labs-bolt-t-shirt")
    assert inventory_page.get_num_of_items_in_cart() == 0


def test_remove_all_from_cart(driver, ):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login_as_standard_user()

    inventory_page.add_to_cart_by_name("sauce-labs-fleece-jacket")
    inventory_page.add_to_cart_by_name("sauce-labs-bike-light")
    inventory_page.add_to_cart_by_name("sauce-labs-bolt-t-shirt")
    assert inventory_page.get_num_of_items_in_cart() == 3

    inventory_page.remove_all_items_inventory_page()

    assert inventory_page.get_num_of_items_in_cart() == 0