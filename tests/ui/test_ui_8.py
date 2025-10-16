"""
UI Test 8: Verify All Products and Product Detail Page
Test Case: Navigate to products page and view product details
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.products
class TestAllProductsAndProductDetail:
    """Test class for all products and product detail page functionality."""
    
    def test_verify_all_products_and_product_detail(self):
        """Test method with screenshot support."""
        try:
"""Test navigation to products page and viewing product details."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        assert "All Products" in products_page.get_products_header_text(), "Products header not correct"
        
        # Verify products list is visible
        assert products_page.are_searched_products_visible(), "Products list not visible"
        
        # Click on first product to view details
        assert products_page.view_product_details(0), "Failed to view product details"
        
        # Verify product detail page is loaded
        assert products_page.is_product_detail_page_loaded(), "Product detail page not loaded"
        
        # Verify product information is visible
        assert products_page.is_product_information_visible(), "Product information not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_all_products_and_product_detail: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_all_products_and_product_detail: {e}")
            raise e
        """Test navigation to products page and viewing product details."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        assert "All Products" in products_page.get_products_header_text(), "Products header not correct"
        
        # Verify products list is visible
        assert products_page.are_searched_products_visible(), "Products list not visible"
        
        # Click on first product to view details
        assert products_page.view_product_details(0), "Failed to view product details"
        
        # Verify product detail page is loaded
        assert products_page.is_product_detail_page_loaded(), "Product detail page not loaded"
        
        # Verify product information is visible
        assert products_page.is_product_information_visible(), "Product information not visible"
    
    def test_verify_products_page_elements(self):
        """Test method with screenshot support."""
        try:
"""Test verification of products page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page elements
        elements_status = products_page.verify_products_page_elements()
        
        assert elements_status['products_header_visible'], "Products header not visible"
        assert elements_status['brand_filter_visible'], "Brand filter not visible"
        assert elements_status['category_filter_visible'], "Category filter not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_products_page_elements: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_products_page_elements: {e}")
            raise e
        """Test verification of products page elements."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page elements
        elements_status = products_page.verify_products_page_elements()
        
        assert elements_status['products_header_visible'], "Products header not visible"
        assert elements_status['brand_filter_visible'], "Brand filter not visible"
        assert elements_status['category_filter_visible'], "Category filter not visible"
    
    def test_verify_product_search_functionality(self):
        """Test method with screenshot support."""
        try:
"""Test product search functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Get search terms from test data
        search_terms = test_data['search_terms']
        
        for search_term in search_terms:
            # Search for product
            assert products_page.search_product(search_term), f"Failed to search for {search_term}"
            
            # Verify search results are visible
            assert products_page.are_searched_products_visible(), f"Search results not visible for {search_term}"
            
            # Get product names and verify they contain search term
            product_names = products_page.get_product_names()
            for product_name in product_names:
                assert search_term.lower() in product_name.lower(), f"Product '{product_name}' does not contain search term '{search_term}'"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_product_search_functionality: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_product_search_functionality: {e}")
            raise e
        """Test product search functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Get search terms from test data
        search_terms = test_data['search_terms']
        
        for search_term in search_terms:
            # Search for product
            assert products_page.search_product(search_term), f"Failed to search for {search_term}"
            
            # Verify search results are visible
            assert products_page.are_searched_products_visible(), f"Search results not visible for {search_term}"
            
            # Get product names and verify they contain search term
            product_names = products_page.get_product_names()
            for product_name in product_names:
                assert search_term.lower() in product_name.lower(), f"Product '{product_name}' does not contain search term '{search_term}'"
    
    def test_verify_add_to_cart_functionality(self, driver, home_page, products_page):
        """Test add to cart functionality from products page."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Add first product to cart
        assert products_page.add_product_to_cart(0), "Failed to add product to cart"
        
        # Handle continue shopping modal if present
        try:
            continue_button = driver.find_element_by_xpath("//button[@class='btn btn-success close-modal btn-block']")
            continue_button.click()
        except:
            pass  # Modal not present or already handled
    
    def test_verify_product_categories(self):
        """Test method with screenshot support."""
        try:
"""Test product categories functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Test category filters
        assert products_page.click_women_category(), "Failed to click Women category"
        assert products_page.click_men_category(), "Failed to click Men category"
        assert products_page.click_kids_category(), "Failed to click Kids category"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_product_categories: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_product_categories: {e}")
            raise e
        """Test product categories functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Test category filters
        assert products_page.click_women_category(), "Failed to click Women category"
        assert products_page.click_men_category(), "Failed to click Men category"
        assert products_page.click_kids_category(), "Failed to click Kids category"
