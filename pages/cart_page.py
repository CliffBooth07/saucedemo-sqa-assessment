from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    BACKPACK = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def wait_until_loaded(self):
        self.wait.until(ec.text_to_be_present_in_element(self.TITLE, "Your Cart"))
        return self

    def product_name(self):
        return self.wait.until(ec.visibility_of_element_located(self.BACKPACK)).text

    def checkout(self):
        def click_until_checkout(driver):
            if "checkout-step-one.html" in driver.current_url:
                return True
            checkout_button = self.wait.until(ec.element_to_be_clickable(self.CHECKOUT_BUTTON))
            checkout_button.click()
            if "checkout-step-one.html" not in driver.current_url:
                driver.execute_script("arguments[0].click();", checkout_button)
            return "checkout-step-one.html" in driver.current_url

        self.wait.until(click_until_checkout)
