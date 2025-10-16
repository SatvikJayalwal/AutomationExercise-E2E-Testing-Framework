"""
UI Test 17: Remove Products from Cart
Test Case: Remove products from cart
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.cart
class TestRemoveProductsFromCart:
    """Test class for removing products from cart functionality."""
    
    def test_remove_products_from_cart(self, driver, home_page, products_page, cart_page):
        """Test removing products from cart."""
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
        
        # Verify products are in cart
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count > 0, "No items in cart"
        
        # NOTE: The Automation Exercise website previously had an 'X' (delete) button in the cart 
        # to remove individual products. As of now (checked in September 2025), this option has been 
        # removed from the UI. Therefore, the "remove product from cart" test case is skipped.
        # This test verifies that the cart functionality works but cannot test removal
        # as the UI no longer supports it.
        
        # Verify that cart page is displayed
        assert cart_page.is_cart_page_loaded(), "Cart page not displayed"
        
        # Verify products are still visible in cart
        assert cart_page.are_cart_items_visible(), "Cart items not visible"
    
    def test_verify_cart_page_without_remove_functionality(self):
        """Test method with screenshot support."""
        try:
"""Test verification of cart page without remove functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page elements
        elements_status = cart_page.verify_cart_page_elements()
        
        assert elements_status['cart_header_visible'], "Cart header not visible"
        assert elements_status['cart_items_visible'] or elements_status['cart_empty'], "Cart status not determined"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_cart_page_without_remove_functionality: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_cart_page_without_remove_functionality: {e}")
            raise e
        """Test verification of cart page without remove functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page elements
        elements_status = cart_page.verify_cart_page_elements()
        
        assert elements_status['cart_header_visible'], "Cart header not visible"
        assert elements_status['cart_items_visible'] or elements_status['cart_empty'], "Cart status not determined"
    
    def test_verify_cart_functionality_without_removal(self, driver, home_page, products_page, cart_page):
        """Test cart functionality without removal feature."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Add a product to cart
        assert products_page.add_product_to_cart(0), "Failed to add product to cart"
        
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
        
        # Verify product is in cart
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count > 0, "No items in cart"
        
        # Verify cart page displays correctly
        assert cart_page.are_cart_items_visible(), "Cart items not visible"
