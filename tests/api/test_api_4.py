"""
API Test 4: Search Product
API URL: https://automationexercise.com/api/searchProduct
Request Method: GET
Response Code: 200
Response JSON: Search results
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.regression
class TestSearchProduct:
    """Test class for search product API."""
    
    def test_search_product_by_name(self):
        """Test method with screenshot support."""
        try:
"""Test search product by name."""
        # Get search terms from test data
        search_terms = test_data['search_terms']
        
        for search_term in search_terms:
            # API endpoint with search parameter
            url = f"{API_BASE_URL}/searchProduct"
            params = {'search_product': search_term}
            
            # Make API request
            response = APIHelper.make_request('GET', url, params=params)
            
            # Assertions
            assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
            assert 'json' in response, "Response should contain JSON data"
            
            # Log response for debugging
            print(f"Search term: {search_term}")
            print(f"Status Code: {response['status_code']}")
            if response.get('json'):
                print(f"Search results count: {len(response['json'].get('products', []))}")
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_by_name: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_by_name: {e}")
            raise e
        """Test search product by name."""
        # Get search terms from test data
        search_terms = test_data['search_terms']
        
        for search_term in search_terms:
            # API endpoint with search parameter
            url = f"{API_BASE_URL}/searchProduct"
            params = {'search_product': search_term}
            
            # Make API request
            response = APIHelper.make_request('GET', url, params=params)
            
            # Assertions
            assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
            assert 'json' in response, "Response should contain JSON data"
            
            # Log response for debugging
            print(f"Search term: {search_term}")
            print(f"Status Code: {response['status_code']}")
            if response.get('json'):
                print(f"Search results count: {len(response['json'].get('products', []))}")
    
    def test_search_product_with_empty_query(self):
        """Test method with screenshot support."""
        try:
"""Test search product with empty query."""
        url = f"{API_BASE_URL}/searchProduct"
        params = {'search_product': ''}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        # Should still return 200 with empty results
        assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_with_empty_query: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_with_empty_query: {e}")
            raise e
        """Test search product with empty query."""
        url = f"{API_BASE_URL}/searchProduct"
        params = {'search_product': ''}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        # Should still return 200 with empty results
        assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
    
    def test_search_product_with_special_characters(self):
        """Test method with screenshot support."""
        try:
"""Test search product with special characters."""
        special_terms = ['@#$%', 'test@example', 'product&item', 'search+term']
        
        for term in special_terms:
            url = f"{API_BASE_URL}/searchProduct"
            params = {'search_product': term}
            
            response = APIHelper.make_request('GET', url, params=params)
            
            # Should handle special characters gracefully
            assert response['status_code'] in [200, 400], f"Unexpected status code for term '{term}': {response['status_code']}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_with_special_characters: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_with_special_characters: {e}")
            raise e
        """Test search product with special characters."""
        special_terms = ['@#$%', 'test@example', 'product&item', 'search+term']
        
        for term in special_terms:
            url = f"{API_BASE_URL}/searchProduct"
            params = {'search_product': term}
            
            response = APIHelper.make_request('GET', url, params=params)
            
            # Should handle special characters gracefully
            assert response['status_code'] in [200, 400], f"Unexpected status code for term '{term}': {response['status_code']}"
    
    def test_search_product_case_sensitivity(self):
        """Test method with screenshot support."""
        try:
"""Test search product case sensitivity."""
        base_term = "dress"
        case_variations = ["dress", "Dress", "DRESS", "DrEsS"]
        
        for term in case_variations:
            url = f"{API_BASE_URL}/searchProduct"
            params = {'search_product': term}
            
            response = APIHelper.make_request('GET', url, params=params)
            
            assert response['status_code'] == 200, f"Search failed for term '{term}'"
            print(f"Case variation '{term}' - Status: {response['status_code']}")
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_case_sensitivity: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_case_sensitivity: {e}")
            raise e
        """Test search product case sensitivity."""
        base_term = "dress"
        case_variations = ["dress", "Dress", "DRESS", "DrEsS"]
        
        for term in case_variations:
            url = f"{API_BASE_URL}/searchProduct"
            params = {'search_product': term}
            
            response = APIHelper.make_request('GET', url, params=params)
            
            assert response['status_code'] == 200, f"Search failed for term '{term}'"
            print(f"Case variation '{term}' - Status: {response['status_code']}")
    
    def test_search_product_response_structure(self):
        """Test method with screenshot support."""
        try:
"""Test search product response structure."""
        search_term = test_data['search_terms'][0]
        url = f"{API_BASE_URL}/searchProduct"
        params = {'search_product': search_term}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        assert response['status_code'] == 200
        json_data = response['json']
        
        # Validate response structure
        assert isinstance(json_data, dict), "Response should be a dictionary"
        
        # Check if products key exists
        if 'products' in json_data:
            assert isinstance(json_data['products'], list), "Products should be a list"
            
            # Validate each product structure
            for product in json_data['products']:
                required_fields = ['id', 'name', 'price', 'brand', 'category']
                for field in required_fields:
                    if field in product:
                        assert product[field] is not None, f"Product '{field}' should not be None"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_search_product_response_structure: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_search_product_response_structure: {e}")
            raise e
        """Test search product response structure."""
        search_term = test_data['search_terms'][0]
        url = f"{API_BASE_URL}/searchProduct"
        params = {'search_product': search_term}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        assert response['status_code'] == 200
        json_data = response['json']
        
        # Validate response structure
        assert isinstance(json_data, dict), "Response should be a dictionary"
        
        # Check if products key exists
        if 'products' in json_data:
            assert isinstance(json_data['products'], list), "Products should be a list"
            
            # Validate each product structure
            for product in json_data['products']:
                required_fields = ['id', 'name', 'price', 'brand', 'category']
                for field in required_fields:
                    if field in product:
                        assert product[field] is not None, f"Product '{field}' should not be None"
