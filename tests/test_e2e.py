from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_full_purchase_flow(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login_as_standard_user()

    inventory.add_to_cart_by_name("sauce-labs-backpack")
    inventory.open_cart()
    assert cart.get_cart_items_count() == 1
    cart.open_checkout()

    checkout.enter_all_information("Meow", "Haw", "00001")
    checkout.continue_checkout()

    checkout.finish_checkout()
    assert "checkout-complete" in driver.current_url