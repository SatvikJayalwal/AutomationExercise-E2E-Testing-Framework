"""
UI Test 12: Add Products in Cart
Test Case: Add multiple products to cart
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.cart
class TestAddProductsInCart:
    """Test class for adding products to cart functionality."""
    
    def test_add_products_in_cart(self, driver, home_page, products_page, cart_page):
        """Test adding multiple products to cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Get product names before adding
        first_product_name = products_page.get_product_names()[0] if products_page.get_product_names() else "Product 1"
        second_product_name = products_page.get_product_names()[1] if len(products_page.get_product_names()) > 1 else "Product 2"
        
        # Add first product to cart
        assert products_page.add_product_to_cart(0), "Failed to add first product to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Add second product to cart
        assert products_page.add_product_to_cart(1), "Failed to add second product to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Go to Cart
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify Cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Verify products in Cart
        cart_product_names = cart_page.get_product_names_in_cart()
        assert first_product_name in cart_product_names, f"{first_product_name} not found in cart"
        assert second_product_name in cart_product_names, f"{second_product_name} not found in cart"
        
        # Verify Price, Quantity, Total
        cart_prices = cart_page.get_product_prices_in_cart()
        for price in cart_prices:
            assert price.startswith("Rs."), f"Price format invalid: {price}"
    
    def test_add_single_product_to_cart(self, driver, home_page, products_page, cart_page):
        """Test adding single product to cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Add first product to cart
        assert products_page.add_product_to_cart(0), "Failed to add product to cart"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Go to Cart
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify Cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Verify product is in cart
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count > 0, "No items in cart"
    
    def test_add_multiple_products_to_cart(self, driver, home_page, products_page, cart_page):
        """Test adding multiple products to cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Add multiple products to cart
        products_to_add = [0, 1, 2]  # Add first 3 products
        
        for product_index in products_to_add:
            # Add product to cart
            assert products_page.add_product_to_cart(product_index), f"Failed to add product {product_index} to cart"
            
            # Click 'Continue Shopping' button
            try:
                continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
                continue_button.click()
            except:
                pass  # Modal not present or already handled
        
        # Go to Cart
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify Cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Verify multiple products in cart
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count >= len(products_to_add), f"Expected at least {len(products_to_add)} items in cart, got {cart_items_count}"
    
    def test_verify_cart_page_functionality(self):
        """Test method with screenshot support."""
        try:
"""Test cart page functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page elements
        elements_status = cart_page.verify_cart_page_elements()
        
        assert elements_status['cart_header_visible'], "Cart header not visible"
        assert elements_status['cart_items_visible'] or elements_status['cart_empty'], "Cart status not determined"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_cart_page_functionality: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_cart_page_functionality: {e}")
            raise e
        """Test cart page functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page elements
        elements_status = cart_page.verify_cart_page_elements()
        
        assert elements_status['cart_header_visible'], "Cart header not visible"
        assert elements_status['cart_items_visible'] or elements_status['cart_empty'], "Cart status not determined"
    
    def test_verify_empty_cart(self):
        """Test method with screenshot support."""
        try:
"""Test empty cart functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Check if cart is empty
        if cart_page.is_cart_empty():
            assert cart_page.get_empty_cart_message() == "Cart is empty!", "Incorrect empty cart message"
        else:
            # If cart has items, verify they are displayed
            assert cart_page.are_cart_items_visible(), "Cart items not visible"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_empty_cart: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_empty_cart: {e}")
            raise e
        """Test empty cart functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Cart button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify cart page is loaded
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Check if cart is empty
        if cart_page.is_cart_empty():
            assert cart_page.get_empty_cart_message() == "Cart is empty!", "Incorrect empty cart message"
        else:
            # If cart has items, verify they are displayed
            assert cart_page.are_cart_items_visible(), "Cart items not visible"
