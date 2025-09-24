# API 10: POST To Verify Login with invalid details
# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: POST
# Request Parameters: email, password (invalid values)
# Response Code: 404
# Response Message: User not found!

import requests
import json

# API URL
url = "https://automationexercise.com/api/verifyLogin"

# Payload: invalid email and password
payload = {
    "email": "invalid@example.com",
    "password": "wrongpassword"
}

# Send POST request
response = requests.post(url, data=payload)

# Capture status code
status = response.status_code
print(f"Status Code : {status}")

# Response text
response_text = response.text
print("Response text:", response_text)

# Expected vs Actual check
if status != 404:
    print(f"[BUG] Expected 404 (Not Found), but got {status}")

# Validate that response body contains the right message
assert "User not found" in response_text, "Unexpected response message!"