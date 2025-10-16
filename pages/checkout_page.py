"""
Checkout page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class CheckoutPage(BasePage):
    """Checkout page class containing locators and methods for the checkout page."""
    
    # Checkout page locators
    CHECKOUT_HEADER = (By.XPATH, "//h2[@class='title text-center']")
    ORDER_REVIEW = (By.XPATH, "//div[@class='review-payment']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[@class='btn btn-default check_out']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert-success alert']")
    REGISTER_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']/u")
    DELIVERY_ADDRESS = (By.XPATH, "//ul[@id='address_delivery']")
    BILLING_ADDRESS = (By.XPATH, "//ul[@id='address_invoice']")
    ORDER_PRODUCTS = (By.XPATH, "//a[@href='/product_details/31']")
    ORDER_COMMENT = (By.XPATH, "//textarea[@class='form-control']")
    PAYMENT_PAGE_HEADER = (By.XPATH, "//div[@class='step-one']/h2")
    NAME_ON_CARD = (By.XPATH, "//input[@data-qa='name-on-card']")
    CARD_NUMBER = (By.XPATH, "//input[@data-qa='card-number']")
    CVC = (By.XPATH, "//input[@data-qa='cvc']")
    EXPIRY_MONTH = (By.XPATH, "//input[@data-qa='expiry-month']")
    EXPIRY_YEAR = (By.XPATH, "//input[@data-qa='expiry-year']")
    PAY_BUTTON = (By.XPATH, "//button[@data-qa='pay-button']")
    CONTINUE_AFTER_ORDER_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/checkout"
    
    def navigate_to_checkout(self) -> bool:
        """Navigate to the checkout page."""
        return self.navigate_to_url(self.page_url)
    
    def is_checkout_page_loaded(self) -> bool:
        """Check if checkout page is loaded."""
        return self.helper.is_element_displayed(self.CHECKOUT_HEADER)
    
    def get_checkout_header_text(self) -> str:
        """Get the checkout page header text."""
        return self.helper.get_element_text(self.CHECKOUT_HEADER)
    
    def is_order_review_visible(self) -> bool:
        """Check if order review is visible."""
        return self.helper.is_element_displayed(self.ORDER_REVIEW)
    
    def place_order(self) -> bool:
        """Click place order button."""
        return self.helper.click_element(self.PLACE_ORDER_BUTTON)
    
    def is_order_successful(self) -> bool:
        """Check if order was placed successfully."""
        return self.helper.is_element_displayed(self.ORDER_SUCCESS_MESSAGE)
    
    def get_order_success_message(self) -> str:
        """Get the order success message."""
        return self.helper.get_element_text(self.ORDER_SUCCESS_MESSAGE)
    
    def click_register_login(self) -> bool:
        """Click register/login button."""
        return self.helper.click_element(self.REGISTER_LOGIN_BUTTON)
    
    def verify_delivery_address(self) -> bool:
        """Verify delivery address is visible."""
        return self.helper.is_element_displayed(self.DELIVERY_ADDRESS)
    
    def verify_billing_address(self) -> bool:
        """Verify billing address is visible."""
        return self.helper.is_element_displayed(self.BILLING_ADDRESS)
    
    def verify_addresses_match(self) -> bool:
        """Verify delivery and billing addresses match."""
        try:
            delivery_text = self.helper.get_element_text(self.DELIVERY_ADDRESS)
            billing_text = self.helper.get_element_text(self.BILLING_ADDRESS)
            return delivery_text.strip() == billing_text.strip()
        except Exception as e:
            logger.error(f"Failed to verify addresses match: {e}")
            return False
    
    def verify_order_products(self) -> bool:
        """Verify order products are visible."""
        return self.helper.is_element_displayed(self.ORDER_PRODUCTS)
    
    def enter_order_comment(self, comment: str) -> bool:
        """Enter order comment."""
        return self.helper.send_keys_to_element(self.ORDER_COMMENT, comment)
    
    def is_payment_page_loaded(self) -> bool:
        """Check if payment page is loaded."""
        return self.helper.is_element_displayed(self.PAYMENT_PAGE_HEADER)
    
    def fill_payment_details(self, name: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str) -> bool:
        """Fill payment details."""
        try:
            # Fill name on card
            if not self.helper.send_keys_to_element(self.NAME_ON_CARD, name):
                return False
            
            # Fill card number
            if not self.helper.send_keys_to_element(self.CARD_NUMBER, card_number):
                return False
            
            # Fill CVC
            if not self.helper.send_keys_to_element(self.CVC, cvc):
                return False
            
            # Fill expiry month
            if not self.helper.send_keys_to_element(self.EXPIRY_MONTH, expiry_month):
                return False
            
            # Fill expiry year
            if not self.helper.send_keys_to_element(self.EXPIRY_YEAR, expiry_year):
                return False
            
            logger.info("Payment details filled successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to fill payment details: {e}")
            return False
    
    def pay_and_confirm_order(self) -> bool:
        """Click pay and confirm order button."""
        return self.helper.click_element(self.PAY_BUTTON)
    
    def get_order_success_message(self) -> str:
        """Get the order success message."""
        return self.helper.get_element_text(self.ORDER_SUCCESS_MESSAGE)
    
    def click_continue_after_order(self) -> bool:
        """Click continue button after order."""
        return self.helper.click_element(self.CONTINUE_AFTER_ORDER_BUTTON)
    
    def verify_checkout_page_elements(self) -> dict:
        """Verify all checkout page elements and return status."""
        return {
            'checkout_header_visible': self.is_checkout_page_loaded(),
            'order_review_visible': self.is_order_review_visible()
        }
