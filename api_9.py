# API 9: DELETE To Verify Login
# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: DELETE
# Expected Response Code: 405
# Expected Response Message: "This request method is not supported."

import requests
import json

# API URL
url = "https://automationexercise.com/api/verifyLogin"

# Send DELETE request
response = requests.delete(url)

# Capture status code
status = response.status_code
print(f"Status Code : {status}")

# Response text
response_text = response.text
print("Response text:", response_text)

# Expected vs Actual check
if status != 405:
    print(f"[BUG] Expected 405 (Method Not Allowed), but got {status}")

# Validate that response body contains the right message
assert "This request method is not supported" in response_text, "Unexpected response message!"