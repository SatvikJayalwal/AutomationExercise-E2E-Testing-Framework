"""
UI Test 13: Verify Product Quantity in Cart
Test Case: Verify product quantity in cart
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
class TestProductQuantityInCart:
    """Test class for verifying product quantity in cart."""
    
    def test_verify_product_quantity_in_cart(self, driver, home_page, products_page, cart_page, test_data):
        """Test verifying product quantity in cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Click on specific product to view details
        assert products_page.view_product_details(11), "Failed to view product details"  # Product 12 (0-indexed)
        
        # Verify product detail page is loaded
        assert products_page.is_product_detail_page_loaded(), "Product detail page not loaded"
        
        # Get product name
        product_name = products_page.get_product_name_from_detail_page()
        
        # Increase quantity to 4
        quantity = 4
        assert products_page.set_product_quantity(quantity), f"Failed to set quantity to {quantity}"
        
        # Click 'Add to cart' button
        assert products_page.add_to_cart_from_detail_page(), "Failed to add product to cart from detail page"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Click 'View Cart' button
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify that Cart page is loaded successfully
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        # Verify product is in cart with correct quantity
        cart_product_names = cart_page.get_product_names_in_cart()
        assert product_name in cart_product_names, f"Product '{product_name}' not found in cart"
        
        # Verify quantity
        cart_quantities = cart_page.get_product_quantities_in_cart()
        for cart_quantity in cart_quantities:
            if cart_quantity == str(quantity):
                break
        else:
            assert False, f"Expected quantity {quantity} not found in cart"
    
    def test_verify_product_quantity_with_different_values(self, driver, home_page, products_page, cart_page):
        """Test verifying product quantity with different values."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test different quantities
        quantities_to_test = [1, 2, 3, 5]
        
        for quantity in quantities_to_test:
            # Click on first product to view details
            assert products_page.view_product_details(0), f"Failed to view product details for quantity {quantity}"
            
            # Set quantity
            assert products_page.set_product_quantity(quantity), f"Failed to set quantity to {quantity}"
            
            # Add to cart
            assert products_page.add_to_cart_from_detail_page(), f"Failed to add product to cart with quantity {quantity}"
            
            # Click 'Continue Shopping' button
            try:
                continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
                continue_button.click()
            except:
                pass  # Modal not present or already handled
            
            # Go to cart to verify
            assert home_page.click_cart(), "Failed to click Cart button"
            
            # Verify quantity in cart
            cart_quantities = cart_page.get_product_quantities_in_cart()
            assert str(quantity) in cart_quantities, f"Quantity {quantity} not found in cart"
            
            # Navigate back to products for next test
            assert home_page.click_products(), "Failed to navigate back to products"
    
    def test_verify_cart_quantity_validation(self):
        """Test method with screenshot support."""
        try:
"""Test cart quantity validation."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test with zero quantity
        assert products_page.view_product_details(0), "Failed to view product details"
        assert products_page.set_product_quantity(0), "Failed to set quantity to 0"
        
        # Try to add to cart with zero quantity
        # This should either be prevented or handled gracefully
        result = products_page.add_to_cart_from_detail_page()
        # The behavior depends on the website implementation
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_cart_quantity_validation: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_cart_quantity_validation: {e}")
            raise e
        """Test cart quantity validation."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test with zero quantity
        assert products_page.view_product_details(0), "Failed to view product details"
        assert products_page.set_product_quantity(0), "Failed to set quantity to 0"
        
        # Try to add to cart with zero quantity
        # This should either be prevented or handled gracefully
        result = products_page.add_to_cart_from_detail_page()
        # The behavior depends on the website implementation
    
    def test_verify_cart_quantity_with_large_numbers(self, driver, home_page, products_page, cart_page):
        """Test cart quantity with large numbers."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test with large quantity
        large_quantity = 100
        assert products_page.view_product_details(0), "Failed to view product details"
        assert products_page.set_product_quantity(large_quantity), f"Failed to set quantity to {large_quantity}"
        
        # Add to cart
        assert products_page.add_to_cart_from_detail_page(), f"Failed to add product to cart with quantity {large_quantity}"
        
        # Click 'Continue Shopping' button
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
        
        # Go to cart to verify
        assert home_page.click_cart(), "Failed to click Cart button"
        
        # Verify quantity in cart
        cart_quantities = cart_page.get_product_quantities_in_cart()
        assert str(large_quantity) in cart_quantities, f"Quantity {large_quantity} not found in cart"
