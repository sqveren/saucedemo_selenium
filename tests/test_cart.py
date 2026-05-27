from pages.cart_page import CartPage


def  test_cart_count(driver, logged_in_inventory):
    cart_page = CartPage(driver)

    logged_in_inventory.add_to_cart_by_name("sauce-labs-fleece-jacket")
    logged_in_inventory.add_to_cart_by_name("sauce-labs-bike-light")

    logged_in_inventory.open_cart()
    item_count = cart_page.get_cart_items_count()

    assert item_count == 2


def test_remove_all_cart_items(driver,logged_in_inventory):
    cart_page = CartPage(driver)

    logged_in_inventory.add_to_cart_by_name("sauce-labs-fleece-jacket")
    logged_in_inventory.add_to_cart_by_name("sauce-labs-bike-light")

    logged_in_inventory.open_cart()
    cart_page.remove_all_from_cart()
    item_count = cart_page.is_cart_empty()

    assert item_count is True

def test_checkout_button_opens_checkout(driver, logged_in_inventory):
        cart_page = CartPage(driver)

        logged_in_inventory.add_to_cart_by_name("sauce-labs-bike-light")
        logged_in_inventory.open_cart()

        cart_page.go_to_checkout()

        assert "checkout-step-one" in driver.current_url

def test_continue_shopping_returns_to_inventory(driver, logged_in_inventory):
        cart_page = CartPage(driver)

        logged_in_inventory.open_cart()
        cart_page.back_to_shopping()

        assert "inventory" in driver.current_url

def test_empty_cart_after_removing_all_items(driver, logged_in_inventory):
        cart_page = CartPage(driver)

        logged_in_inventory.add_to_cart_by_name("sauce-labs-fleece-jacket")

        logged_in_inventory.open_cart()

        cart_page.remove_all_from_cart()

        assert cart_page.get_cart_items_count() == 0

