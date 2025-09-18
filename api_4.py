# API 4: PUT To All Brands List
# API URL: https://automationexercise.com/api/brandsList
# Request Method: PUT
# Expected Response Code: 405
# Expected Response Message: "This request method is not supported."

import requests
import json

# API URL
url = "https://automationexercise.com/api/brandsList"

# Send PUT request
response = requests.put(url)

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