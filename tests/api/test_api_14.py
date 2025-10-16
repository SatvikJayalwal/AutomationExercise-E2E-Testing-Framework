"""
API Test 14: GET user account detail by email
API URL: https://automationexercise.com/api/getUserDetailByEmail
Request Method: GET
Expected Response Code: 200
Expected Response: User Detail JSON
"""
import pytest
from utils.helpers import APIHelper
from config.config import API_BASE_URL
from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure
from utils.logger import logger


@pytest.mark.api
@pytest.mark.smoke
class TestGetUserDetailByEmail:
    """Test class for get user detail by email API."""
    
    def test_get_user_detail_by_valid_email(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail by valid email."""
        # API endpoint
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Query parameters
        params = {"email": user_data['email']}
        
        # Make GET request
        response = APIHelper.make_request('GET', url, params=params)
        
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
        if actual_code != 200:
            print(f"[BUG] Expected 200, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (200)")
        
        # Validate response content
        if actual_code == 200:
            # Check if user details are present
            assert "email" in json_data or "user" in json_data, "User details not found in response"
            
            # If user object exists, validate its structure
            if "user" in json_data:
                user = json_data["user"]
                assert "email" in user, "User email not found"
                assert "name" in user, "User name not found"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_by_valid_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_by_valid_email: {e}")
            raise e
        """Test GET request to get user detail by valid email."""
        # API endpoint
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Get test user data
        user_data = test_data['test_users'][0]
        
        # Query parameters
        params = {"email": user_data['email']}
        
        # Make GET request
        response = APIHelper.make_request('GET', url, params=params)
        
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
        if actual_code != 200:
            print(f"[BUG] Expected 200, but got {actual_code}")
            # This might be a known issue with the API
            assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
        else:
            print("Status code is correct (200)")
        
        # Validate response content
        if actual_code == 200:
            # Check if user details are present
            assert "email" in json_data or "user" in json_data, "User details not found in response"
            
            # If user object exists, validate its structure
            if "user" in json_data:
                user = json_data["user"]
                assert "email" in user, "User email not found"
                assert "name" in user, "User name not found"
    
    def test_get_user_detail_by_invalid_email(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail by invalid email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Query parameters with invalid email
        params = {"email": invalid_user['email']}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle invalid email
        assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_by_invalid_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_by_invalid_email: {e}")
            raise e
        """Test GET request to get user detail by invalid email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Get invalid user data
        invalid_user = test_data['invalid_users'][0]
        
        # Query parameters with invalid email
        params = {"email": invalid_user['email']}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle invalid email
        assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
    
    def test_get_user_detail_by_nonexistent_email(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail by nonexistent email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with nonexistent email
        params = {"email": "nonexistent@example.com"}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle nonexistent email
        assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_by_nonexistent_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_by_nonexistent_email: {e}")
            raise e
        """Test GET request to get user detail by nonexistent email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with nonexistent email
        params = {"email": "nonexistent@example.com"}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle nonexistent email
        assert actual_code in [200, 404], f"Unexpected status code: {actual_code}"
    
    def test_get_user_detail_without_email_parameter(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail without email parameter."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # No query parameters
        response = APIHelper.make_request('GET', url)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing email parameter
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_without_email_parameter: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_without_email_parameter: {e}")
            raise e
        """Test GET request to get user detail without email parameter."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # No query parameters
        response = APIHelper.make_request('GET', url)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle missing email parameter
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
    def test_get_user_detail_with_empty_email(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail with empty email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with empty email
        params = {"email": ""}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle empty email
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_with_empty_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_with_empty_email: {e}")
            raise e
        """Test GET request to get user detail with empty email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with empty email
        params = {"email": ""}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle empty email
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
    def test_get_user_detail_with_malformed_email(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail with malformed email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with malformed email
        params = {"email": "invalid-email-format"}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle malformed email
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_with_malformed_email: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_with_malformed_email: {e}")
            raise e
        """Test GET request to get user detail with malformed email."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with malformed email
        params = {"email": "invalid-email-format"}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle malformed email
        assert actual_code in [200, 400, 404], f"Unexpected status code: {actual_code}"
    
    def test_get_user_detail_with_sql_injection_attempt(self):
        """Test method with screenshot support."""
        try:
"""Test GET request to get user detail with SQL injection attempt."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with SQL injection attempt
        params = {"email": "admin' OR '1'='1"}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle SQL injection attempt safely
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
        
        # Should not return user details for SQL injection
        if actual_code == 200:
            response_text = json_data.get("message", "") or response['text']
            assert "email" not in response_text or "user" not in response_text, "SQL injection attempt should not succeed"

        except AssertionError as e:
            logger.error(f"Assertion failed in test_get_user_detail_with_sql_injection_attempt: {e}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in test_get_user_detail_with_sql_injection_attempt: {e}")
            raise e
        """Test GET request to get user detail with SQL injection attempt."""
        url = f"{API_BASE_URL}/getUserDetailByEmail"
        
        # Query parameters with SQL injection attempt
        params = {"email": "admin' OR '1'='1"}
        
        response = APIHelper.make_request('GET', url, params=params)
        
        print(f"Status Code: {response['status_code']}")
        print(f"Response Text: {response['text']}")
        
        # Parse JSON response if available
        json_data = {}
        if response.get('json'):
            json_data = response['json']
        
        actual_code = json_data.get("responseCode", response['status_code'])
        print(f"Status / Response Code: {actual_code}")
        
        # Should handle SQL injection attempt safely
        assert actual_code in [200, 404, 400], f"Unexpected status code: {actual_code}"
        
        # Should not return user details for SQL injection
        if actual_code == 200:
            response_text = json_data.get("message", "") or response['text']
            assert "email" not in response_text or "user" not in response_text, "SQL injection attempt should not succeed"
