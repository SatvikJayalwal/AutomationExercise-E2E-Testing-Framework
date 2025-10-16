"""
UI Test 14: Place Order: Register while Checkout
Test Case: Complete checkout process with registration
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.checkout
class TestPlaceOrderRegisterWhileCheckout:
    """Test class for placing order with registration during checkout."""
    
    def test_place_order_register_while_checkout(self, driver, home_page, products_page, cart_page, checkout_page, login_page, signup_page, account_info_page, test_data):
        """Test complete checkout process with registration."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
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
        
        # Click 'Register / Login' button
        assert checkout_page.click_register_login(), "Failed to click Register / Login button"
        
        # Verify 'New User Signup!' is visible
        assert login_page.is_signup_form_visible(), "New User Signup form not visible"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Enter name and email address
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start signup process"
        
        # Verify that 'ENTER ACCOUNT INFORMATION' is visible
        assert signup_page.is_account_info_form_visible(), "Account information form not visible"
        
        # Complete signup process
        assert signup_page.complete_signup(user_data), "Failed to complete signup process"
        
        # Verify account created message
        assert signup_page.is_account_created(), "Account created message not visible"
        
        # Click continue button
        assert signup_page.click_continue(), "Failed to click continue button"
        
        # Verify user is logged in
        assert home_page.is_logged_in(), "User not logged in after registration"
        
        # Click 'Cart' button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is displayed
        assert cart_page.is_cart_page_loaded(), "Cart page not displayed"
        
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
        
        # Click 'Delete Account' button
        assert home_page.click_delete_account(), "Failed to click Delete Account button"
        
        # Verify that 'ACCOUNT DELETED!' is visible
        assert account_info_page.is_account_deleted_message_visible(), "Account deleted message not visible"
        assert "ACCOUNT DELETED!" in account_info_page.get_account_deleted_message(), "Incorrect account deleted message"
        
        # Click 'Continue' button
        assert account_info_page.click_continue(), "Failed to click continue button"
    
    def test_verify_checkout_page_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of checkout page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add some products to cart first
        # This is a simplified version - in real scenario, you'd add products first
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Verify checkout page elements
        elements_status = checkout_page.verify_checkout_page_elements()
        
        assert elements_status['checkout_header_visible'], "Checkout header not visible"
        assert elements_status['order_review_visible'], "Order review not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_checkout_page_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_checkout_page_elements: {e}")
            raise e
        """Test verification of checkout page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add some products to cart first
        # This is a simplified version - in real scenario, you'd add products first
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Verify checkout page elements
        elements_status = checkout_page.verify_checkout_page_elements()
        
        assert elements_status['checkout_header_visible'], "Checkout header not visible"
        assert elements_status['order_review_visible'], "Order review not visible"
    
    def test_verify_payment_page_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of payment page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add some products to cart first
        # This is a simplified version - in real scenario, you'd add products first
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Navigate to payment page (simplified)
        # In real scenario, you'd go through the full checkout process
        
        # Verify payment page elements
        assert checkout_page.is_payment_page_loaded(), "Payment page not loaded"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_payment_page_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_payment_page_elements: {e}")
            raise e
        """Test verification of payment page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add some products to cart first
        # This is a simplified version - in real scenario, you'd add products first
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Navigate to payment page (simplified)
        # In real scenario, you'd go through the full checkout process
        
        # Verify payment page elements
        assert checkout_page.is_payment_page_loaded(), "Payment page not loaded"
