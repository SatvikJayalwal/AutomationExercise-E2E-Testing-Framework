"""
UI Test 20: Search Products and Verify Cart After Login
Test Case: Search products and verify cart persistence after login
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.search
class TestSearchProductsAndVerifyCartAfterLogin:
    """Test class for searching products and verifying cart persistence after login."""
    
    def test_search_products_and_verify_cart_after_login(self, driver, home_page, products_page, cart_page, login_page, test_data):
        """Test search products and verify cart persistence after login."""
        screenshot_manager = ScreenshotManager(driver)
        
        try:
            # Navigate to home page
            assert home_page.navigate_to_home(), "Failed to navigate to home page"
            assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
            
            # Search for products
            assert home_page.click_products(), "Failed to click Products button"
            assert products_page.is_all_products_text_visible(), "Products page not visible"
            
            # Search for a specific product
            search_term = "tshirt"
            assert products_page.enter_product_name_in_search(search_term), "Failed to enter search term"
            assert products_page.click_search_button(), "Failed to click search button"
            assert products_page.is_searched_products_visible(), "Searched products not visible"
            
            # Add products to cart
            assert products_page.add_product_to_cart(0), "Failed to add first product to cart"
            assert products_page.click_continue_shopping_button(), "Failed to click continue shopping"
            assert products_page.add_product_to_cart(1), "Failed to add second product to cart"
            assert products_page.click_continue_shopping_button(), "Failed to click continue shopping"
            
            # Go to cart and verify products
            assert home_page.click_cart(), "Failed to click Cart button"
            assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
            
            # Login to account
            assert home_page.click_signup_login(), "Failed to click Signup/Login button"
            assert login_page.is_login_form_visible(), "Login form not visible"
            
            user_data = test_data['test_users'][0]
            assert login_page.login(user_data['email'], user_data['password']), "Failed to login"
            
            # Verify user is logged in
            assert home_page.is_logged_in(), "User not logged in after login"
            
            # Go back to cart and verify products are still there
            assert home_page.click_cart(), "Failed to click Cart button after login"
            assert cart_page.is_cart_page_loaded(), "Cart page not loaded after login"
            
            # Verify cart has products
            cart_products = cart_page.get_product_names_in_cart()
            assert len(cart_products) > 0, "Cart is empty after login"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_products_and_verify_cart_after_login: {e}")
            screenshot_manager.take_screenshot_on_assertion_failure(str(e), "test_search_products_and_verify_cart_after_login")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_products_and_verify_cart_after_login: {e}")
            screenshot_manager.take_screenshot_on_error(str(e), "test_search_products_and_verify_cart_after_login")
            raise e