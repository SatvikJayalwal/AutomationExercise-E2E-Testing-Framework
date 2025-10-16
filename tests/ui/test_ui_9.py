"""
UI Test 9: Search Product
Test Case: Search for products
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.products
class TestSearchProduct:
    """Test class for product search functionality."""
    
    def test_search_product(self):
        """Test method with screenshot support."""
        try:
"""Test product search functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Get search terms from test data
        search_terms = test_data['search_terms']
        
        for search_term in search_terms:
            # Search for product
            assert products_page.search_product(search_term), f"Failed to search for {search_term}"
            
            # Verify 'SEARCHED PRODUCTS' is visible
            assert products_page.are_searched_products_visible(), f"Search results not visible for {search_term}"
            
            # Verify all products related to search are visible
            product_names = products_page.get_product_names()
            for product_name in product_names:
                assert search_term.lower() in product_name.lower(), f"Product '{product_name}' does not contain search term '{search_term}'"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product: {e}")
            raise e
        """Test product search functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Get search terms from test data
        search_terms = test_data['search_terms']
        
        for search_term in search_terms:
            # Search for product
            assert products_page.search_product(search_term), f"Failed to search for {search_term}"
            
            # Verify 'SEARCHED PRODUCTS' is visible
            assert products_page.are_searched_products_visible(), f"Search results not visible for {search_term}"
            
            # Verify all products related to search are visible
            product_names = products_page.get_product_names()
            for product_name in product_names:
                assert search_term.lower() in product_name.lower(), f"Product '{product_name}' does not contain search term '{search_term}'"
    
    def test_search_product_with_specific_term(self):
        """Test method with screenshot support."""
        try:
"""Test product search with specific search term."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search for specific product
        search_term = "Premium Polo T-Shirts"
        assert products_page.search_product(search_term), f"Failed to search for {search_term}"
        
        # Verify search results
        assert products_page.are_searched_products_visible(), "Search results not visible"
        
        # Verify all products contain the search term
        product_names = products_page.get_product_names()
        for product_name in product_names:
            assert search_term.lower() in product_name.lower(), f"Product '{product_name}' does not contain search term '{search_term}'"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_with_specific_term: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_with_specific_term: {e}")
            raise e
        """Test product search with specific search term."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search for specific product
        search_term = "Premium Polo T-Shirts"
        assert products_page.search_product(search_term), f"Failed to search for {search_term}"
        
        # Verify search results
        assert products_page.are_searched_products_visible(), "Search results not visible"
        
        # Verify all products contain the search term
        product_names = products_page.get_product_names()
        for product_name in product_names:
            assert search_term.lower() in product_name.lower(), f"Product '{product_name}' does not contain search term '{search_term}'"
    
    def test_search_product_with_empty_query(self):
        """Test method with screenshot support."""
        try:
"""Test product search with empty query."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search with empty query
        assert products_page.search_product(""), "Failed to search with empty query"
        
        # Should still show products or handle empty search gracefully
        # The behavior depends on the website implementation
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_with_empty_query: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_with_empty_query: {e}")
            raise e
        """Test product search with empty query."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search with empty query
        assert products_page.search_product(""), "Failed to search with empty query"
        
        # Should still show products or handle empty search gracefully
        # The behavior depends on the website implementation
    
    def test_search_product_with_special_characters(self):
        """Test method with screenshot support."""
        try:
"""Test product search with special characters."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search with special characters
        special_terms = ["@#$%", "test@example", "product&item", "search+term"]
        
        for term in special_terms:
            # Search for product
            assert products_page.search_product(term), f"Failed to search for {term}"
            
            # Should handle special characters gracefully
            # The behavior depends on the website implementation
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_with_special_characters: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_with_special_characters: {e}")
            raise e
        """Test product search with special characters."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search with special characters
        special_terms = ["@#$%", "test@example", "product&item", "search+term"]
        
        for term in special_terms:
            # Search for product
            assert products_page.search_product(term), f"Failed to search for {term}"
            
            # Should handle special characters gracefully
            # The behavior depends on the website implementation
    
    def test_search_product_case_sensitivity(self):
        """Test method with screenshot support."""
        try:
"""Test product search case sensitivity."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test case sensitivity
        base_term = "dress"
        case_variations = ["dress", "Dress", "DRESS", "DrEsS"]
        
        for term in case_variations:
            # Search for product
            assert products_page.search_product(term), f"Failed to search for {term}"
            
            # Should handle case variations
            # The behavior depends on the website implementation
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_case_sensitivity: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_case_sensitivity: {e}")
            raise e
        """Test product search case sensitivity."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test case sensitivity
        base_term = "dress"
        case_variations = ["dress", "Dress", "DRESS", "DrEsS"]
        
        for term in case_variations:
            # Search for product
            assert products_page.search_product(term), f"Failed to search for {term}"
            
            # Should handle case variations
            # The behavior depends on the website implementation
    
    def test_search_product_with_nonexistent_term(self):
        """Test method with screenshot support."""
        try:
"""Test product search with nonexistent search term."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search for nonexistent product
        search_term = "nonexistentproduct123"
        assert products_page.search_product(search_term), f"Failed to search for {search_term}"
        
        # Should handle nonexistent search term gracefully
        # The behavior depends on the website implementation

        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_with_nonexistent_term: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_with_nonexistent_term: {e}")
            raise e
        """Test product search with nonexistent search term."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Products button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Search for nonexistent product
        search_term = "nonexistentproduct123"
        assert products_page.search_product(search_term), f"Failed to search for {search_term}"
        
        # Should handle nonexistent search term gracefully
        # The behavior depends on the website implementation
