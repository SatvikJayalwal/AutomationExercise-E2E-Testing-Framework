"""
API Test 1: Get All Products List
API URL: https://automationexercise.com/api/productsList
Request Method: GET
Response Code: 200
Response JSON: All products list
"""
import pytest
from utils.helpers import APIHelper
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from config.config import API_BASE_URL
from utils.logger import logger


@pytest.mark.api
@pytest.mark.smoke
class TestGetAllProductsList:
    """Test class for getting all products list API."""
    
    def test_get_all_products_list(self):
        """Test GET request to products list API."""
        try:
            # API endpoint
            url = f"{API_BASE_URL}/productsList"
            logger.info(f"Making API request to: {url}")
            
            # Make API request
            response = APIHelper.make_request('GET', url)
            
            # Assertions
            assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
            assert 'json' in response, "Response should contain JSON data"
            assert 'products' in response['json'], "'products' key not found in response"
            assert len(response['json']['products']) > 0, "Product list is empty"
            
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_all_products_list: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error: {e}")
            raise e
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Total Products: {len(response['json']['products'])}")
        
        # Additional validations
        products = response['json']['products']
        for product in products[:3]:  # Check first 3 products
            assert 'id' in product, "Product should have 'id' field"
            assert 'name' in product, "Product should have 'name' field"
            assert 'price' in product, "Product should have 'price' field"
            assert 'brand' in product, "Product should have 'brand' field"
            assert 'category' in product, "Product should have 'category' field"
    
    def test_get_all_products_list_response_structure(self):
        """Test the structure of products list response."""
        try:
            url = f"{API_BASE_URL}/productsList"
            response = APIHelper.make_request('GET', url)
            
            assert response['status_code'] == 200
            json_data = response['json']
            
            # Validate response structure
            assert isinstance(json_data, dict), "Response should be a dictionary"
            assert 'products' in json_data, "Response should contain 'products' key"
            assert isinstance(json_data['products'], list), "Products should be a list"
            
            # Validate each product structure
            for product in json_data['products']:
                required_fields = ['id', 'name', 'price', 'brand', 'category']
                for field in required_fields:
                    assert field in product, f"Product should have '{field}' field"
                    assert product[field] is not None, f"Product '{field}' should not be None"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_all_products_list_response_structure: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_all_products_list_response_structure: {e}")
            raise e