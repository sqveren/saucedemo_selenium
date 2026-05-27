from pages.checkout_page import CheckoutPage



def test_checkout_with_information(driver, logged_and_checkout_page):

    logged_and_checkout_page.enter_all_information(
        "Meow",
        "Haw",
        "00001"
    )

    assert "checkout-step-two" in driver.current_url


def test_checkout_without_name(driver, logged_and_checkout_page):
    logged_and_checkout_page.enter_all_information(
        "",
        "Haw",
        "00001"
    )

    logged_and_checkout_page.continue_checkout()

    assert "First Name is required" in logged_and_checkout_page.get_error_message()

def test_checkout_without_surname(driver, logged_and_checkout_page):
    logged_and_checkout_page.enter_all_information(
        "Meow",
        "",
        "00001"
    )

    logged_and_checkout_page.continue_checkout()

    assert "Last Name is required" in logged_and_checkout_page.get_error_message()


def test_checkout_without_zip(driver, logged_and_checkout_page):
    logged_and_checkout_page.enter_all_information(
        "Meow",
        "Haw",
        ""
    )

    logged_and_checkout_page.continue_checkout()

    assert "Postal Code is required" in logged_and_checkout_page.get_error_message()

def test_checkout_complete_flow(driver, logged_and_checkout_page):

    logged_and_checkout_page.enter_all_information(
        "Meow",
        "Haw",
        "00001"
    )

    logged_and_checkout_page.continue_checkout()

    assert "checkout-step-two" in driver.current_url

    logged_and_checkout_page.finish_checkout()

    assert "checkout-complete" in driver.current_url

def test_cancel_checkout(driver, logged_and_checkout_page):

    logged_and_checkout_page.cancel_checkout()

    assert "inventory" in driver.current_url