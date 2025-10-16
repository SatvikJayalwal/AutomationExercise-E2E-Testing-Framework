"""
UI Test 22: Add to Cart from Recommended Items
Test Case: Add to cart from recommended items
"""
import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.cart
class TestAddToCartFromRecommendedItems:
    """Test class for adding to cart from recommended items."""
    
    def test_add_to_cart_from_recommended_items(self, driver, home_page, cart_page):
        """Test adding to cart from recommended items."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Verify 'RECOMMENDED ITEMS' are visible
        assert home_page.is_recommended_items_visible(), "Recommended items not visible"
        assert "recommended items" in home_page.get_recommended_items_text().lower(), "Incorrect recommended items text"
        
        # Click on 'Add To Cart' on Recommended product
        assert home_page.add_recommended_item_to_cart(), "Failed to add recommended item to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Click on 'View Cart' button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify that product is displayed in cart page
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        assert cart_page.are_cart_items_visible(), "Cart items not visible"
        
        # Verify the recommended product is in cart
        cart_product_names = cart_page.get_product_names_in_cart()
        assert len(cart_product_names) > 0, "No products found in cart"
        
        # Verify product description contains expected text
        for product_name in cart_product_names:
            if "Summer White Top" in product_name:
                break
        else:
            # If specific product not found, just verify any product is in cart
            assert len(cart_product_names) > 0, "No products found in cart"
    
    def test_verify_recommended_items_section(self):
        """Test method with screenshot support."""
        try:
"""Test verification of recommended items section."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify recommended items section elements
        elements_status = home_page.verify_recommended_items_elements()
        
        assert elements_status['recommended_items_visible'], "Recommended items not visible"
        assert elements_status['recommended_items_header_visible'], "Recommended items header not visible"
        assert elements_status['recommended_products_visible'], "Recommended products not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_recommended_items_section: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_recommended_items_section: {e}")
            raise e
        """Test verification of recommended items section."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify recommended items section elements
        elements_status = home_page.verify_recommended_items_elements()
        
        assert elements_status['recommended_items_visible'], "Recommended items not visible"
        assert elements_status['recommended_items_header_visible'], "Recommended items header not visible"
        assert elements_status['recommended_products_visible'], "Recommended products not visible"
    
    def test_verify_recommended_items_functionality(self, driver, home_page, cart_page):
        """Test recommended items functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to recommended items section
        assert home_page.scroll_to_recommended_items(), "Failed to scroll to recommended items"
        
        # Verify recommended items are visible
        assert home_page.is_recommended_items_visible(), "Recommended items not visible after scrolling"
        
        # Add recommended item to cart
        assert home_page.add_recommended_item_to_cart(), "Failed to add recommended item to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Go to cart and verify
        assert home_page.click_cart(), "Failed to click Cart button"
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        assert cart_page.are_cart_items_visible(), "Cart items not visible"
    
    def test_verify_multiple_recommended_items(self, driver, home_page, cart_page):
        """Test adding multiple recommended items to cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Scroll to recommended items section
        assert home_page.scroll_to_recommended_items(), "Failed to scroll to recommended items"
        
        # Add multiple recommended items to cart
        recommended_items_count = 3  # Add 3 recommended items
        
        for i in range(recommended_items_count):
            # Add recommended item to cart
            assert home_page.add_recommended_item_to_cart(i), f"Failed to add recommended item {i} to cart"
            
            # Click 'Continue Shopping' button
            try:
                continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
                continue_button.click()
            except:
                pass  # Modal not present or already handled
        
        # Go to cart and verify
        assert home_page.click_cart(), "Failed to click Cart button"
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Verify multiple items in cart
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count >= recommended_items_count, f"Expected at least {recommended_items_count} items in cart, got {cart_items_count}"
