"""
UI Test 19: View & Cart Brand Products
Test Case: View and add brand products to cart
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.products
class TestViewCartBrandProducts:
    """Test class for viewing and adding brand products to cart."""
    
    def test_view_cart_brand_products(self):
        """Test method with screenshot support."""
        try:
"""Test viewing and adding brand products to cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Verify that Brands are visible on left side bar
        assert products_page.is_brand_filter_visible(), "Brands not visible on left sidebar"
        
        # Click on any brand name
        assert products_page.click_brand_hm(), "Failed to click H&M brand"
        
        # Verify that user is navigated to brand page and brand products are displayed
        assert products_page.is_brand_hm_products_visible(), "H&M brand products not displayed"
        assert "Brand - H&M Products" in products_page.get_brand_hm_products_text(), "Incorrect brand text"
        
        # On left side bar, click on any other brand link
        assert products_page.click_brand_polo(), "Failed to click Polo brand"
        
        # Verify that user is navigated to that brand page and can see products
        assert products_page.is_brand_polo_products_visible(), "Polo brand products not displayed"
        assert "Brand - Polo Products" in products_page.get_brand_polo_products_text(), "Incorrect brand text"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_view_cart_brand_products: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_view_cart_brand_products: {e}")
            raise e
        """Test viewing and adding brand products to cart."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Verify products page is loaded
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        
        # Verify that Brands are visible on left side bar
        assert products_page.is_brand_filter_visible(), "Brands not visible on left sidebar"
        
        # Click on any brand name
        assert products_page.click_brand_hm(), "Failed to click H&M brand"
        
        # Verify that user is navigated to brand page and brand products are displayed
        assert products_page.is_brand_hm_products_visible(), "H&M brand products not displayed"
        assert "Brand - H&M Products" in products_page.get_brand_hm_products_text(), "Incorrect brand text"
        
        # On left side bar, click on any other brand link
        assert products_page.click_brand_polo(), "Failed to click Polo brand"
        
        # Verify that user is navigated to that brand page and can see products
        assert products_page.is_brand_polo_products_visible(), "Polo brand products not displayed"
        assert "Brand - Polo Products" in products_page.get_brand_polo_products_text(), "Incorrect brand text"
    
    def test_verify_brand_navigation(self):
        """Test method with screenshot support."""
        try:
"""Test brand navigation functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test H&M brand
        assert products_page.click_brand_hm(), "Failed to click H&M brand"
        assert products_page.is_brand_hm_products_visible(), "H&M brand products not visible"
        
        # Navigate back to products
        assert home_page.click_products(), "Failed to navigate back to products"
        
        # Test Polo brand
        assert products_page.click_brand_polo(), "Failed to click Polo brand"
        assert products_page.is_brand_polo_products_visible(), "Polo brand products not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_brand_navigation: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_brand_navigation: {e}")
            raise e
        """Test brand navigation functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test H&M brand
        assert products_page.click_brand_hm(), "Failed to click H&M brand"
        assert products_page.is_brand_hm_products_visible(), "H&M brand products not visible"
        
        # Navigate back to products
        assert home_page.click_products(), "Failed to navigate back to products"
        
        # Test Polo brand
        assert products_page.click_brand_polo(), "Failed to click Polo brand"
        assert products_page.is_brand_polo_products_visible(), "Polo brand products not visible"
    
    def test_verify_brand_products_display(self):
        """Test method with screenshot support."""
        try:
"""Test verification of brand products display."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Click on H&M brand
        assert products_page.click_brand_hm(), "Failed to click H&M brand"
        
        # Verify brand products are displayed
        assert products_page.are_brand_products_visible(), "Brand products not visible"
        
        # Verify product information
        product_names = products_page.get_product_names()
        assert len(product_names) > 0, "No products found for brand"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_brand_products_display: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_brand_products_display: {e}")
            raise e
        """Test verification of brand products display."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Click on H&M brand
        assert products_page.click_brand_hm(), "Failed to click H&M brand"
        
        # Verify brand products are displayed
        assert products_page.are_brand_products_visible(), "Brand products not visible"
        
        # Verify product information
        product_names = products_page.get_product_names()
        assert len(product_names) > 0, "No products found for brand"
    
    def test_verify_all_brand_links(self):
        """Test method with screenshot support."""
        try:
"""Test verification of all brand links."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test different brands
        brands = ['H&M', 'Polo', 'Madame', 'Mast & Harbour', 'Babyhug', 'Allen Solly', 'Kookie Kids', 'Biba']
        
        for brand in brands:
            # Click on brand
            if brand == 'H&M':
                assert products_page.click_brand_hm(), f"Failed to click {brand} brand"
            elif brand == 'Polo':
                assert products_page.click_brand_polo(), f"Failed to click {brand} brand"
            # Add more brand methods as needed
            
            # Navigate back to products for next brand
            assert home_page.click_products(), f"Failed to navigate back to products for {brand}"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_all_brand_links: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_all_brand_links: {e}")
            raise e
        """Test verification of all brand links."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click 'Products' button
        assert home_page.click_products(), "Failed to click Products button"
        
        # Test different brands
        brands = ['H&M', 'Polo', 'Madame', 'Mast & Harbour', 'Babyhug', 'Allen Solly', 'Kookie Kids', 'Biba']
        
        for brand in brands:
            # Click on brand
            if brand == 'H&M':
                assert products_page.click_brand_hm(), f"Failed to click {brand} brand"
            elif brand == 'Polo':
                assert products_page.click_brand_polo(), f"Failed to click {brand} brand"
            # Add more brand methods as needed
            
            # Navigate back to products for next brand
            assert home_page.click_products(), f"Failed to navigate back to products for {brand}"
