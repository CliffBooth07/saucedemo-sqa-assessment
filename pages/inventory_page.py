from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    def wait_until_loaded(self):
        self.wait.until(ec.text_to_be_present_in_element(self.TITLE, "Products"))
        return self

    def add_backpack(self):
        add_button = self.wait.until(ec.element_to_be_clickable(self.ADD_BACKPACK))
        add_button.click()
        self.wait.until(ec.presence_of_element_located(self.CART_BADGE))
        return self

    def cart_count(self):
        return self.wait.until(ec.presence_of_element_located(self.CART_BADGE)).text

    def open_cart(self):
        cart_link = self.wait.until(ec.element_to_be_clickable(self.CART_LINK))
        cart_link.click()
        try:
            WebDriverWait(self.driver, 2).until(ec.url_contains("cart.html"))
        except TimeoutException:
            self.driver.execute_script("arguments[0].click();", cart_link)
            self.wait.until(ec.url_contains("cart.html"))
