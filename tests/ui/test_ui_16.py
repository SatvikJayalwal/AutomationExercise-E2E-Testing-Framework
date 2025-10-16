"""
UI Test 16: Place Order: Login before Checkout
Test Case: Complete checkout process with login before checkout
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.checkout
class TestPlaceOrderLoginBeforeCheckout:
    """Test class for placing order with login before checkout."""
    
    def test_place_order_login_before_checkout(self, driver, home_page, products_page, cart_page, checkout_page, login_page, test_data):
        """Test complete checkout process with login before checkout."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Add multiple products to cart
        products_to_add = [30, 34, 42]  # Product IDs 31, 35, 43 (0-indexed)
        
        for product_index in products_to_add:
            # Add product to cart
            assert products_page.add_product_to_cart(product_index), f"Failed to add product {product_index} to cart"
            
            # Click 'Continue Shopping' button
            try:
                continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
                continue_button.click()
            except:
                pass  # Modal not present or already handled
        
        # Click 'Cart' button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Click on 'Signup / Login' button
        assert checkout_page.click_register_login(), "Failed to click Register / Login button"
        
        # Verify 'Login to your account' is visible
        assert login_page.is_login_form_visible(), "Login form not visible"
        
        # Get test user credentials
        user_credentials = test_data['user_credentials']
        
        # Enter correct email address and password
        assert login_page.login(user_credentials['valid_email'], user_credentials['valid_password']), "Failed to login"
        
        # Verify that 'Logged in as username' is visible
        assert login_page.is_logged_in_visible(), "Logged in message not visible"
        
        # Click 'Cart' button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Verify Address Details
        assert checkout_page.verify_delivery_address(), "Delivery address not visible"
        assert checkout_page.verify_billing_address(), "Billing address not visible"
        assert checkout_page.verify_addresses_match(), "Addresses do not match"
        
        # Review Your Order
        assert checkout_page.verify_order_products(), "Order products not visible"
        
        # Enter description in comment text area
        assert checkout_page.enter_order_comment("Test description..."), "Failed to enter order comment"
        
        # Click 'Place Order'
        assert checkout_page.place_order(), "Failed to click Place Order"
        
        # Verify payment page is loaded
        assert checkout_page.is_payment_page_loaded(), "Payment page not loaded"
        
        # Fill payment details
        assert checkout_page.fill_payment_details(
            "Test User",
            "123456789",
            "069",
            "11",
            "2060"
        ), "Failed to fill payment details"
        
        # Click 'Pay and Confirm Order' button
        assert checkout_page.pay_and_confirm_order(), "Failed to pay and confirm order"
        
        # Verify success message
        assert checkout_page.is_order_successful(), "Order not placed successfully"
        assert "ORDER PLACED!" in checkout_page.get_order_success_message(), "Incorrect success message"
        
        # Click 'Continue' button
        assert checkout_page.click_continue_after_order(), "Failed to click continue after order"
    
    def test_verify_login_before_checkout_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of login before checkout elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add some products to cart first
        # This is a simplified version - in real scenario, you'd add products first
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Click on 'Signup / Login' button
        assert checkout_page.click_register_login(), "Failed to click Register / Login button"
        
        # Verify login page elements
        elements_status = login_page.verify_login_page_elements()
        
        assert elements_status['login_form_visible'], "Login form not visible"
        assert elements_status['signup_form_visible'], "Signup form not visible"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_before_checkout_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_before_checkout_elements: {e}")
            raise e
        """Test verification of login before checkout elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add some products to cart first
        # This is a simplified version - in real scenario, you'd add products first
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Click on 'Signup / Login' button
        assert checkout_page.click_register_login(), "Failed to click Register / Login button"
        
        # Verify login page elements
        elements_status = login_page.verify_login_page_elements()
        
        assert elements_status['login_form_visible'], "Login form not visible"
        assert elements_status['signup_form_visible'], "Signup form not visible"
