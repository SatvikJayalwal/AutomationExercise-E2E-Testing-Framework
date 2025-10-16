"""
UI Test 18: View Category Products
Test Case: View products by category
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.products
class TestViewCategoryProducts:
    """Test class for viewing products by category."""
    
    def test_view_category_products(self):
        """Test method with screenshot support."""
        try:
"""Test viewing products by category."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Verify that categories are visible on left side bar
        assert home_page.is_categories_visible(), "Categories not visible on left sidebar"
        
        # Click on 'Women' category
        assert home_page.click_women_category(), "Failed to click Women category"
        
        # Click on any category link under 'Women' category, for example: Tops
        assert products_page.click_women_tops(), "Failed to click Women Tops category"
        
        # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
        assert products_page.is_women_tops_products_visible(), "Women - Tops Products not displayed"
        assert "Women - Tops Products" in products_page.get_women_tops_products_text(), "Incorrect category text"
        
        # Click on 'Men' category
        assert home_page.click_men_category(), "Failed to click Men category"
        
        # Click on any category link under 'Men' category, for example: Jeans
        assert products_page.click_men_jeans(), "Failed to click Men Jeans category"
        
        # Verify that user is navigated to that category page
        assert products_page.is_men_jeans_products_visible(), "Men - Jeans Products not displayed"
        assert "Men - Jeans Products" in products_page.get_men_jeans_products_text(), "Incorrect category text"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_view_category_products: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_view_category_products: {e}")
            raise e
        """Test viewing products by category."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        assert home_page.is_home_page_loaded(), "Home page not loaded successfully"
        
        # Verify that categories are visible on left side bar
        assert home_page.is_categories_visible(), "Categories not visible on left sidebar"
        
        # Click on 'Women' category
        assert home_page.click_women_category(), "Failed to click Women category"
        
        # Click on any category link under 'Women' category, for example: Tops
        assert products_page.click_women_tops(), "Failed to click Women Tops category"
        
        # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
        assert products_page.is_women_tops_products_visible(), "Women - Tops Products not displayed"
        assert "Women - Tops Products" in products_page.get_women_tops_products_text(), "Incorrect category text"
        
        # Click on 'Men' category
        assert home_page.click_men_category(), "Failed to click Men category"
        
        # Click on any category link under 'Men' category, for example: Jeans
        assert products_page.click_men_jeans(), "Failed to click Men Jeans category"
        
        # Verify that user is navigated to that category page
        assert products_page.is_men_jeans_products_visible(), "Men - Jeans Products not displayed"
        assert "Men - Jeans Products" in products_page.get_men_jeans_products_text(), "Incorrect category text"
    
    def test_verify_category_navigation(self):
        """Test method with screenshot support."""
        try:
"""Test category navigation functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify categories are visible
        assert home_page.is_categories_visible(), "Categories not visible"
        
        # Test Women category
        assert home_page.click_women_category(), "Failed to click Women category"
        assert products_page.click_women_tops(), "Failed to click Women Tops"
        assert products_page.is_women_tops_products_visible(), "Women Tops products not visible"
        
        # Navigate back to home
        assert home_page.navigate_to_home(), "Failed to navigate back to home"
        
        # Test Men category
        assert home_page.click_men_category(), "Failed to click Men category"
        assert products_page.click_men_jeans(), "Failed to click Men Jeans"
        assert products_page.is_men_jeans_products_visible(), "Men Jeans products not visible"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_category_navigation: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_category_navigation: {e}")
            raise e
        """Test category navigation functionality."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Verify categories are visible
        assert home_page.is_categories_visible(), "Categories not visible"
        
        # Test Women category
        assert home_page.click_women_category(), "Failed to click Women category"
        assert products_page.click_women_tops(), "Failed to click Women Tops"
        assert products_page.is_women_tops_products_visible(), "Women Tops products not visible"
        
        # Navigate back to home
        assert home_page.navigate_to_home(), "Failed to navigate back to home"
        
        # Test Men category
        assert home_page.click_men_category(), "Failed to click Men category"
        assert products_page.click_men_jeans(), "Failed to click Men Jeans"
        assert products_page.is_men_jeans_products_visible(), "Men Jeans products not visible"
    
    def test_verify_category_products_display(self):
        """Test method with screenshot support."""
        try:
"""Test verification of category products display."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Women category
        assert home_page.click_women_category(), "Failed to click Women category"
        assert products_page.click_women_tops(), "Failed to click Women Tops"
        
        # Verify category products are displayed
        assert products_page.are_category_products_visible(), "Category products not visible"
        
        # Verify product information
        product_names = products_page.get_product_names()
        assert len(product_names) > 0, "No products found in category"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_category_products_display: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_category_products_display: {e}")
            raise e
        """Test verification of category products display."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Click on Women category
        assert home_page.click_women_category(), "Failed to click Women category"
        assert products_page.click_women_tops(), "Failed to click Women Tops"
        
        # Verify category products are displayed
        assert products_page.are_category_products_visible(), "Category products not visible"
        
        # Verify product information
        product_names = products_page.get_product_names()
        assert len(product_names) > 0, "No products found in category"
    
    def test_verify_all_category_links(self):
        """Test method with screenshot support."""
        try:
"""Test verification of all category links."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Test Women categories
        women_categories = ['Tops', 'Dress']
        for category in women_categories:
            assert home_page.click_women_category(), f"Failed to click Women category for {category}"
            # Navigate to specific women category
            # This would need specific methods for each category
            assert home_page.navigate_to_home(), "Failed to navigate back to home"
        
        # Test Men categories
        men_categories = ['Jeans', 'Tshirts']
        for category in men_categories:
            assert home_page.click_men_category(), f"Failed to click Men category for {category}"
            # Navigate to specific men category
            # This would need specific methods for each category
            assert home_page.navigate_to_home(), "Failed to navigate back to home"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_all_category_links: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_all_category_links: {e}")
            raise e
        """Test verification of all category links."""
        # Navigate to home page
        assert home_page.navigate_to_home(), "Failed to navigate to home page"
        
        # Test Women categories
        women_categories = ['Tops', 'Dress']
        for category in women_categories:
            assert home_page.click_women_category(), f"Failed to click Women category for {category}"
            # Navigate to specific women category
            # This would need specific methods for each category
            assert home_page.navigate_to_home(), "Failed to navigate back to home"
        
        # Test Men categories
        men_categories = ['Jeans', 'Tshirts']
        for category in men_categories:
            assert home_page.click_men_category(), f"Failed to click Men category for {category}"
            # Navigate to specific men category
            # This would need specific methods for each category
            assert home_page.navigate_to_home(), "Failed to navigate back to home"
