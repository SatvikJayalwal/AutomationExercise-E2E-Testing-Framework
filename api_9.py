# API 9: DELETE To Verify Login
# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: DELETE
# Expected Response Code: 405
# Expected Response Message: "This request method is not supported."

import requests
import json

url = "https://automationexercise.com/api/verifyLogin"

response = requests.delete(url)

# Parse JSON response
try:
    response_json = response.json()
except json.JSONDecodeError:
    response_json = {}
print("Response JSON:", response_json)

# Use responseCode if present, else fallback to HTTP status
actual_code = response_json.get("responseCode", response.status_code)
print(f"Status / Response Code: {actual_code}")

# Expected vs Actual check
if actual_code != 405:
    print(f"[BUG] Expected 405, but got {actual_code}")

# Validate message
expected_msg = "This request method is not supported"
assert expected_msg in response_json.get("message", "") or expected_msg in response.text, "Unexpected response message!"