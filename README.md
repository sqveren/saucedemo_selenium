# Selenium UI Automation Framework (SauceDemo)

## Overview

This project is a UI test automation framework built with Python, Selenium WebDriver, and Pytest.  
It automates testing of the SauceDemo web application, covering core user flows such as login, product inventory, cart operations, and checkout process.

The framework is implemented using the Page Object Model (POM) design pattern to ensure maintainability, scalability, and separation of test logic from page interactions.

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Chrome WebDriver

---

## Project Structure

pages/
base_page.py
login_page.py
inventory_page.py
cart_page.py
checkout_page.py

tests/
test_login.py
test_inventory.py
test_cart.py
test_checkout.py
test_e2e.py

conftest.py
requirements.txt
README.md

---

## Covered Functional Areas

### Login
- Valid login with standard user
- Negative login scenarios

### Inventory Page
- Adding items to cart
- Removing items from cart
- Cart badge validation
- Product sorting validation

### Cart
- Cart content verification
- Removing items from cart
- Navigation to checkout

### Checkout
- Filling checkout form
- Field validation (first name, last name, postal code)
- Complete checkout process
- Cancel checkout flow

---

## End-to-End Scenario

The framework includes a full user journey test:

Login → Add product → Open cart → Checkout → Finish purchase → Verify success

---

## Design Approach

The project follows Page Object Model (POM):

- Each page is represented as a separate class
- Locators are stored inside page objects
- Common Selenium actions are centralized in BasePage
- Tests contain only business logic and assertions

---

## Setup Instructions

### Install dependencies

pip install -r requirements.txt

### Run tests

pytest -v

---

## Notes

- Tests run on Chrome browser
- Explicit waits are used for synchronization
- Framework is designed for learning and portfolio purposes

---

## Future Improvements

- CI/CD integration (GitHub Actions)
- Allure reporting
- Parallel test execution
- Docker support
- API testing layer extension
