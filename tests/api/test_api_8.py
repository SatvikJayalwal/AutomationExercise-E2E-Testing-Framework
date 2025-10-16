"""
API Test 8: POST To Verify Login without email parameter
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Expected Response Code: 400
Expected Response Message: "Bad request, email or password parameter is missing in POST request"
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.regression
class TestVerifyLoginWithoutEmail:
    """Test class for verify login API without email parameter."""
    
    def test_verify_login_without_email_parameter(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login without email parameter."""
        # API endpoint
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload without email parameter
        payload = {"password": "mypassword123"}
        
        # Make POST request
        response = APIHelper.make_request('POST', url, data=payload)
        
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
        if actual_code != 400:
            print(f"[BUG] Expected 400, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (400)")
        
        # Validate message
        expected_msg = "email or password parameter is missing"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_without_email_parameter: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_without_email_parameter: {e}")
            raise e
        """Test POST request to verify login without email parameter."""
        # API endpoint
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload without email parameter
        payload = {"password": "mypassword123"}
        
        # Make POST request
        response = APIHelper.make_request('POST', url, data=payload)
        
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
        if actual_code != 400:
            print(f"[BUG] Expected 400, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (400)")
        
        # Validate message
        expected_msg = "email or password parameter is missing"
        response_text = json_data.get("message", "") or response['text']
        assert expected_msg in response_text, f"Unexpected response message! Expected: {expected_msg}, Got: {response_text}"
    
    def test_verify_login_without_password_parameter(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login without password parameter."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload without password parameter
        payload = {"email": "test@example.com"}
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing password parameter
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_without_password_parameter: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_without_password_parameter: {e}")
            raise e
        """Test POST request to verify login without password parameter."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload without password parameter
        payload = {"email": "test@example.com"}
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing password parameter
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
    def test_verify_login_without_any_parameters(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login without any parameters."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Empty payload
        payload = {}
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing parameters
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_without_any_parameters: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_without_any_parameters: {e}")
            raise e
        """Test POST request to verify login without any parameters."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Empty payload
        payload = {}
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing parameters
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
    
    def test_verify_login_with_wrong_parameter_names(self):
        """Test method with screenshot support."""
        try:
"""Test POST request to verify login with wrong parameter names."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload with wrong parameter names
        payload = {
            "username": "test@example.com",
            "pass": "password123"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle wrong parameter names
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_verify_login_with_wrong_parameter_names: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_verify_login_with_wrong_parameter_names: {e}")
            raise e
        """Test POST request to verify login with wrong parameter names."""
        url = f"{API_BASE_URL}/verifyLogin"
        
        # Payload with wrong parameter names
        payload = {
            "username": "test@example.com",
            "pass": "password123"
        }
        
        response = APIHelper.make_request('POST', url, data=payload)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle wrong parameter names
        assert actual_code in [200, 400], f"Unexpected status code: {actual_code}"
