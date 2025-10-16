"""
Cart page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class CartPage(BasePage):
    """Cart page class containing locators and methods for the cart page."""
    
    # Cart page locators
    CART_HEADER = (By.XPATH, "//h2[@class='title text-center']")
    CART_ITEMS = (By.XPATH, "//tr[@id='product-1']")
    PRODUCT_NAMES = (By.XPATH, "//td[@class='cart_description']//h4")
    PRODUCT_PRICES = (By.XPATH, "//td[@class='cart_price']//p")
    PRODUCT_QUANTITIES = (By.XPATH, "//td[@class='cart_quantity']//button")
    TOTAL_PRICES = (By.XPATH, "//td[@class='cart_total_price']//p")
    DELETE_BUTTONS = (By.XPATH, "//a[@class='cart_quantity_delete']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[@class='btn btn-default check_out']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//b[contains(text(), 'Cart is empty!')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/view_cart"
    
    def navigate_to_cart(self) -> bool:
        """Navigate to the cart page."""
        return self.navigate_to_url(self.page_url)
    
    def is_cart_page_loaded(self) -> bool:
        """Check if cart page is loaded."""
        return self.helper.is_element_displayed(self.CART_HEADER)
    
    def get_cart_header_text(self) -> str:
        """Get the cart page header text."""
        return self.helper.get_element_text(self.CART_HEADER)
    
    def are_cart_items_visible(self) -> bool:
        """Check if cart items are visible."""
        return self.helper.is_element_displayed(self.CART_ITEMS)
    
    def get_cart_items_count(self) -> int:
        """Get the number of items in cart."""
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            return len(items)
        except Exception as e:
            logger.error(f"Failed to get cart items count: {e}")
            return 0
    
    def get_product_names_in_cart(self) -> list:
        """Get list of product names in cart."""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_NAMES)
            return [element.text for element in elements]
        except Exception as e:
            logger.error(f"Failed to get product names in cart: {e}")
            return []
    
    def get_product_prices_in_cart(self) -> list:
        """Get list of product prices in cart."""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_PRICES)
            return [element.text for element in elements]
        except Exception as e:
            logger.error(f"Failed to get product prices in cart: {e}")
            return []
    
    def delete_product_from_cart(self, product_index: int = 0) -> bool:
        """Delete a product from cart by index."""
        try:
            delete_buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
            if product_index < len(delete_buttons):
                delete_buttons[product_index].click()
                logger.info(f"Deleted product {product_index} from cart")
                return True
            else:
                logger.error(f"Product index {product_index} out of range")
                return False
        except Exception as e:
            logger.error(f"Failed to delete product from cart: {e}")
            return False
    
    def proceed_to_checkout(self) -> bool:
        """Click proceed to checkout button."""
        return self.helper.click_element(self.PROCEED_TO_CHECKOUT_BUTTON)
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty."""
        return self.helper.is_element_displayed(self.EMPTY_CART_MESSAGE)
    
    def get_empty_cart_message(self) -> str:
        """Get the empty cart message."""
        return self.helper.get_element_text(self.EMPTY_CART_MESSAGE)
    
    def get_product_quantities_in_cart(self) -> list:
        """Get list of product quantities in cart."""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_QUANTITIES)
            return [element.text for element in elements]
        except Exception as e:
            logger.error(f"Failed to get product quantities in cart: {e}")
            return []
    
    def verify_cart_page_elements(self) -> dict:
        """Verify all cart page elements and return status."""
        return {
            'cart_header_visible': self.is_cart_page_loaded(),
            'cart_items_visible': self.are_cart_items_visible(),
            'cart_empty': self.is_cart_empty()
        }
