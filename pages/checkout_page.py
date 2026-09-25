from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def complete_customer_details(self, first_name, last_name, postal_code):
        self._enter_value(self.FIRST_NAME, first_name)
        self._enter_value(self.LAST_NAME, last_name)
        self._enter_value(self.POSTAL_CODE, postal_code)

        continue_button = self.wait.until(ec.element_to_be_clickable(self.CONTINUE))
        continue_button.click()
        try:
            WebDriverWait(self.driver, 2).until(
                ec.url_contains("checkout-step-two.html")
            )
        except TimeoutException:
            self.driver.execute_script("arguments[0].click();", continue_button)
            self.wait.until(ec.url_contains("checkout-step-two.html"))

        finish_button = self.wait.until(ec.element_to_be_clickable(self.FINISH))
        finish_button.click()
        try:
            self.wait.until(ec.visibility_of_element_located(self.COMPLETE_HEADER))
        except TimeoutException:
            self.driver.execute_script("arguments[0].click();", finish_button)
            self.wait.until(ec.visibility_of_element_located(self.COMPLETE_HEADER))

    def _enter_value(self, locator, value):
        field = self.wait.until(ec.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(value)

        # SauceDemo uses controlled React inputs. Keep a small fallback for
        # runs where send_keys does not update the value held by the page.
        if field.get_attribute("value") != value:
            self.driver.execute_script(
                """
                const field = arguments[0];
                const setter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype, 'value'
                ).set;
                setter.call(field, arguments[1]);
                field.dispatchEvent(new Event('input', {bubbles: true}));
                field.dispatchEvent(new Event('change', {bubbles: true}));
                """,
                field,
                value,
            )

    def confirmation_message(self):
        return self.wait.until(ec.visibility_of_element_located(self.COMPLETE_HEADER)).text
