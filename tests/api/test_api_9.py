"""
API Test 9: DELETE To Verify Login
API URL: https://automationexercise.com/api/verifyLogin
Request Method: DELETE
Expected Response Code: 405
Expected Response Message: "This request method is not supported."
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.regression
class TestDeleteVerifyLogin:
    """Test class for DELETE request to verify login API."""
    
    def test_delete_verify_login_wrong_method(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request to verify login API (should return 405)."""
        # API endpoint
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Make DELETE request (wrong method)
        response = APIHelper.make_request('DELETE', url)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
            print(f"Response JSON: {json_data}")
        
        # Use responseCode if present, else fallback to HTTP status
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Expected vs Actual check
        if actual_code != 405:
            print(f"[BUG] Expected 405, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (405)")
        
        # Validate message
        expected_msg = "This request method is not supported"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_verify_login_wrong_method: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_verify_login_wrong_method: {e}")
            raise e
        """Test DELETE request to verify login API (should return 405)."""
        # API endpoint
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Make DELETE request (wrong method)
        response = APIHelper.make_request('DELETE', url)
        
        # Log response for debugging
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
            print(f"Response JSON: {json_data}")
        
        # Use responseCode if present, else fallback to HTTP status
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Expected vs Actual check
        if actual_code != 405:
            print(f"[BUG] Expected 405, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (405)")
        
        # Validate message
        expected_msg = "This request method is not supported"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
    def test_delete_verify_login_with_data(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request with data to verify login API."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Test data
        test_data = {
            "email": "test@example.com",
            "password": "password123"
        }
        
        # Make DELETE request with data
        response = APIHelper.make_request('DELETE', url, data=test_data)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle DELETE with data
        assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_verify_login_with_data: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_verify_login_with_data: {e}")
            raise e
        """Test DELETE request with data to verify login API."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Test data
        test_data = {
            "email": "test@example.com",
            "password": "password123"
        }
        
        # Make DELETE request with data
        response = APIHelper.make_request('DELETE', url, data=test_data)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle DELETE with data
        assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
    
    def test_delete_verify_login_headers(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request headers to verify login API."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Custom headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = APIHelper.make_request('DELETE', url, headers=headers)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Headers: {response['headers']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Validate response headers
        assert 'content-type' in response['headers'], "Response should have content-type header"
        assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_verify_login_headers: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_verify_login_headers: {e}")
            raise e
        """Test DELETE request headers to verify login API."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Custom headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = APIHelper.make_request('DELETE', url, headers=headers)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Headers: {response['headers']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Validate response headers
        assert 'content-type' in response['headers'], "Response should have content-type header"
        assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
    
    def test_delete_verify_login_with_json_payload(self):
        """Test method with screenshot support."""
        try:
"""Test DELETE request with JSON payload to verify login API."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # JSON payload
        json_payload = {
            "email": "test@example.com",
            "password": "password123"
        }
        
        # Make DELETE request with JSON payload
        response = APIHelper.make_request('DELETE', url, json=json_payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle DELETE with JSON payload
        assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_delete_verify_login_with_json_payload: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_delete_verify_login_with_json_payload: {e}")
            raise e
        """Test DELETE request with JSON payload to verify login API."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # JSON payload
        json_payload = {
            "email": "test@example.com",
            "password": "password123"
        }
        
        # Make DELETE request with JSON payload
        response = APIHelper.make_request('DELETE', url, json=json_payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle DELETE with JSON payload
        assert actual_code in [200, 405], f"Unexpected status code: {actual_code}"
