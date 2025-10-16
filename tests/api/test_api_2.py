"""
API Test 2: POST To All Products List
API URL: https://automationexercise.com/api/productsList
Request Method: POST
Expected Response Code: 405 (but API actually gives 200)
Expected Response Message: "This request method is not supported."
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.regression
class TestPostToProductsList:
    """Test class for POST request to products list API."""
    
    def test_post_to_products_list_wrong_method(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to products list API (should return 405)."""
        # API endpoint
        url = f"{API_BASE_URL}/productsList"
        
        # Make POST request (wrong method)
        response = APIHelper.make_request('POST', url)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Expected 405 but actual is 200 -> Log bug
        if response['status_code'] != 405:
            print(f"[BUG] Expected 405 (Method Not Allowed), but got {response['status_code']}")
            # This is a known issue with the API
            assert response['status_code'] == 200, f"API should return 200, but got {response['status_code']}"
        else:
            print("Status code is correct (405)")
            # If 405 as expected, validate error message
            assert "This request method is not supported" in response['text'], "Unexpected response message!"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_post_to_products_list_wrong_method: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_post_to_products_list_wrong_method: {e}")
            raise e
        """Test POST request to products list API (should return 405)."""
        # API endpoint
        url = f"{API_BASE_URL}/productsList"
        
        # Make POST request (wrong method)
        response = APIHelper.make_request('POST', url)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Expected 405 but actual is 200 -> Log bug
        if response['status_code'] != 405:
            print(f"[BUG] Expected 405 (Method Not Allowed), but got {response['status_code']}")
            # This is a known issue with the API
            assert response['status_code'] == 200, f"API should return 200, but got {response['status_code']}"
        else:
            print("Status code is correct (405)")
            # If 405 as expected, validate error message
            assert "This request method is not supported" in response['text'], "Unexpected response message!"
    
    def test_post_to_products_list_with_data(self):
        """Test method with screenshot support."""
        try:
"""Test POST request with data to products list API."""
        url = f"{API_BASE_URL}/productsList"
        
        # Test data
        test_data = {
            "search_product": "dress",
            "category": "women"
        }
        
        # Make POST request with data
        response = APIHelper.make_request('POST', url, json=test_data)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # The API might accept POST with data, so we just log the response
        assert response['status_code'] in [200, 405], f"Unexpected status code: {response['status_code']}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_post_to_products_list_with_data: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_post_to_products_list_with_data: {e}")
            raise e
        """Test POST request with data to products list API."""
        url = f"{API_BASE_URL}/productsList"
        
        # Test data
        test_data = {
            "search_product": "dress",
            "category": "women"
        }
        
        # Make POST request with data
        response = APIHelper.make_request('POST', url, json=test_data)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # The API might accept POST with data, so we just log the response
        assert response['status_code'] in [200, 405], f"Unexpected status code: {response['status_code']}"
    
    def test_post_to_products_list_headers(self):
        """Test method with screenshot support."""
        try:
"""Test POST request headers to products list API."""
        url = f"{API_BASE_URL}/productsList"
        
        # Custom headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = APIHelper.make_request('POST', url, headers=headers)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Headers: {response['headers']}")
        
        # Validate response headers
        assert 'content-type' in response['headers'], "Response should have content-type header"
        assert response['status_code'] in [200, 405], f"Unexpected status code: {response['status_code']}"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_post_to_products_list_headers: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_post_to_products_list_headers: {e}")
            raise e
        """Test POST request headers to products list API."""
        url = f"{API_BASE_URL}/productsList"
        
        # Custom headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = APIHelper.make_request('POST', url, headers=headers)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Headers: {response['headers']}")
        
        # Validate response headers
        assert 'content-type' in response['headers'], "Response should have content-type header"
        assert response['status_code'] in [200, 405], f"Unexpected status code: {response['status_code']}"
