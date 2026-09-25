import time

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_standard_user_can_complete_purchase(driver):
    """Covers the main revenue path from login to order confirmation."""
    LoginPage(driver).open().login_as("standard_user", "secret_sauce")
    inventory = InventoryPage(driver).wait_until_loaded()

    inventory.add_backpack()
    assert inventory.cart_count() == "1"
    inventory.open_cart()

    cart = CartPage(driver).wait_until_loaded()
    assert cart.product_name() == "Sauce Labs Backpack"
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.complete_customer_details("Test", "Testers", "123456")

    # Keep the confirmation page visible briefly during a headed demo run.
    time.sleep(5)
    assert checkout.confirmation_message() == "Thank you for your order!"
