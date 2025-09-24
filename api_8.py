# API 8: POST To Verify Login without email parameter
# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: POST
# Expected Response Code: 400
# Expected Response Message: "Bad request, email or password parameter is missing in POST request"

import requests
import json

# API URL
url = "https://automationexercise.com/api/verifyLogin"

# Payload: only password, missing email
payload = {
    "password": "123456"
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
if status != 400:
    print(f"[BUG] Expected 400 (Bad Request), but got {status}")

# Validate that response body contains the right message
assert "email or password parameter is missing" in response_text, "Unexpected response message!"