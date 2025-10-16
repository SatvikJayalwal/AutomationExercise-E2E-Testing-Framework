"""
API Test 3: Get All Brands List
API URL: https://automationexercise.com/api/brandsList
Request Method: GET
Response Code: 200
Response JSON: All brands list
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.smoke
class TestGetAllBrandsList:
    """Test class for getting all brands list API."""
    
    def test_get_all_brands_list(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to brands list API."""
        # API endpoint
        url = f"{API_BASE_URL}/brandsList"
        
        # Make API request
        response = APIHelper.make_request('GET', url)
        
        # Assertions
        assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
        assert 'json' in response, "Response should contain JSON data"
        assert 'brands' in response['json'], "'brands' key not found in response"
        assert len(response['json']['brands']) > 0, "Brands list is empty"
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Total Brands: {len(response['json']['brands'])}")
        
        # Additional validations
        brands = response['json']['brands']
        for brand in brands[:3]:  # Check first 3 brands
            assert 'id' in brand, "Brand should have 'id' field"
            assert 'brand' in brand, "Brand should have 'brand' field"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_all_brands_list: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_all_brands_list: {e}")
            raise e
        """Test GET request to brands list API."""
        # API endpoint
        url = f"{API_BASE_URL}/brandsList"
        
        # Make API request
        response = APIHelper.make_request('GET', url)
        
        # Assertions
        assert response['status_code'] == 200, f"Expected 200(OK) but got {response['status_code']}"
        assert 'json' in response, "Response should contain JSON data"
        assert 'brands' in response['json'], "'brands' key not found in response"
        assert len(response['json']['brands']) > 0, "Brands list is empty"
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Total Brands: {len(response['json']['brands'])}")
        
        # Additional validations
        brands = response['json']['brands']
        for brand in brands[:3]:  # Check first 3 brands
            assert 'id' in brand, "Brand should have 'id' field"
            assert 'brand' in brand, "Brand should have 'brand' field"
    
    def test_get_all_brands_list_response_structure(self):
        """Test method with screenshot support."""
        try:
"""Test the structure of brands list response."""
        url = f"{API_BASE_URL}/brandsList"
        response = APIHelper.make_request('GET', url)
        
        assert response['status_code'] == 200
        json_data = response['json']
        
        # Validate response structure
        assert isinstance(json_data, dict), "Response should be a dictionary"
        assert 'brands' in json_data, "Response should contain 'brands' key"
        assert isinstance(json_data['brands'], list), "Brands should be a list"
        
        # Validate each brand structure
        for brand in json_data['brands']:
            required_fields = ['id', 'brand']
            for field in required_fields:
                assert field in brand, f"Brand should have '{field}' field"
                assert brand[field] is not None, f"Brand '{field}' should not be None"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_all_brands_list_response_structure: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_all_brands_list_response_structure: {e}")
            raise e
        """Test the structure of brands list response."""
        url = f"{API_BASE_URL}/brandsList"
        response = APIHelper.make_request('GET', url)
        
        assert response['status_code'] == 200
        json_data = response['json']
        
        # Validate response structure
        assert isinstance(json_data, dict), "Response should be a dictionary"
        assert 'brands' in json_data, "Response should contain 'brands' key"
        assert isinstance(json_data['brands'], list), "Brands should be a list"
        
        # Validate each brand structure
        for brand in json_data['brands']:
            required_fields = ['id', 'brand']
            for field in required_fields:
                assert field in brand, f"Brand should have '{field}' field"
                assert brand[field] is not None, f"Brand '{field}' should not be None"
    
    def test_brands_list_contains_expected_brands(self):
        """Test method with screenshot support."""
        try:
"""Test that brands list contains expected brands."""
        url = f"{API_BASE_URL}/brandsList"
        response = APIHelper.make_request('GET', url)
        
        assert response['status_code'] == 200
        brands = response['json']['brands']
        
        # Expected brands (based on the website)
        expected_brands = ['Polo', 'H&M', 'Madame', 'Mast & Harbour', 'Babyhug', 'Allen Solly Junior', 'Kookie Kids', 'Biba']
        
        # Get actual brand names
        actual_brands = [brand['brand'] for brand in brands]
        
        # Check if expected brands are present
        for expected_brand in expected_brands:
            assert expected_brand in actual_brands, f"Expected brand '{expected_brand}' not found in brands list"
        
        print(f"Found {len(actual_brands)} brands: {actual_brands}")

        except AssertionError as e:
            logger.error(f"Assertion failed in test_brands_list_contains_expected_brands: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_brands_list_contains_expected_brands: {e}")
            raise e
        """Test that brands list contains expected brands."""
        url = f"{API_BASE_URL}/brandsList"
        response = APIHelper.make_request('GET', url)
        
        assert response['status_code'] == 200
        brands = response['json']['brands']
        
        # Expected brands (based on the website)
        expected_brands = ['Polo', 'H&M', 'Madame', 'Mast & Harbour', 'Babyhug', 'Allen Solly Junior', 'Kookie Kids', 'Biba']
        
        # Get actual brand names
        actual_brands = [brand['brand'] for brand in brands]
        
        # Check if expected brands are present
        for expected_brand in expected_brands:
            assert expected_brand in actual_brands, f"Expected brand '{expected_brand}' not found in brands list"
        
        print(f"Found {len(actual_brands)} brands: {actual_brands}")
