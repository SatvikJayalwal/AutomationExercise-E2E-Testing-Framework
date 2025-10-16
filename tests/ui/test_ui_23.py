"""
UI Test 23: Verify Address Details in Checkout Page
Test Case: Verify address details in checkout page
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.checkout
class TestVerifyAddressDetailsInCheckoutPage:
    """Test class for verifying address details in checkout page."""
    
    def test_verify_address_details_in_checkout_page(self, driver, home_page, products_page, cart_page, checkout_page, login_page, signup_page, test_data):
        """Test verifying address details in checkout page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on 'Signup / Login' button
        assert home_page.click_signup_login(), "Failed to click Signup / Login button"
        
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
        
        # Add products to cart
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
        
        # Verify Address Details
        assert checkout_page.verify_delivery_address(), "Delivery address not visible"
        assert checkout_page.verify_billing_address(), "Billing address not visible"
        assert checkout_page.verify_addresses_match(), "Addresses do not match"
        
        # Click 'Delete Account' button
        assert home_page.click_delete_account(), "Failed to click Delete Account button"
        
        # Verify that 'ACCOUNT DELETED!' is visible
        assert signup_page.is_account_deleted_visible(), "Account deleted message not visible"
        assert "ACCOUNT DELETED!" in signup_page.get_account_deleted_message(), "Incorrect account deleted message"
        
        # Click 'Continue' button
        assert signup_page.click_continue(), "Failed to click continue button"
    
    def test_verify_address_details_without_registration(self, driver, home_page, products_page, cart_page, checkout_page):
        """Test verifying address details without registration."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Add products to cart
        assert home_page.click_products(), "Failed to click Products button"
        assert products_page.add_product_to_cart(0), "Failed to add product to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Go to cart
        assert home_page.click_cart(), "Failed to click Cart button"
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Click Proceed To Checkout
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Verify that checkout page shows login/register option
        assert checkout_page.is_register_login_visible(), "Register/Login option not visible"
    
    def test_verify_address_details_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of address details elements."""
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
            logger.error(f"Assertion failed in test_verify_address_details_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_address_details_elements: {e}")
            raise e
        """Test verification of address details elements."""
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
    
    def test_verify_address_consistency(self, driver, home_page, products_page, cart_page, checkout_page, login_page, signup_page, test_data):
        """Test address consistency in checkout."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Register user
        assert home_page.click_signup_login(), "Failed to click Signup / Login button"
        assert login_page.is_signup_form_visible(), "New User Signup form not visible"
        
        user_data = test_data['test_users'][0]
        assert login_page.signup(user_data['name'], user_data['email']), "Failed to start signup process"
        assert signup_page.is_account_info_form_visible(), "Account information form not visible"
        assert signup_page.complete_signup(user_data), "Failed to complete signup process"
        assert signup_page.is_account_created(), "Account created message not visible"
        assert signup_page.click_continue(), "Failed to click continue button"
        
        # Add products and go to checkout
        assert home_page.click_products(), "Failed to click Products button"
        assert products_page.add_product_to_cart(0), "Failed to add product to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        assert home_page.click_cart(), "Failed to click Cart button"
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        assert cart_page.proceed_to_checkout(), "Failed to click Proceed To Checkout"
        
        # Verify address details
        assert checkout_page.verify_delivery_address(), "Delivery address not visible"
        assert checkout_page.verify_billing_address(), "Billing address not visible"
        assert checkout_page.verify_addresses_match(), "Addresses do not match"
