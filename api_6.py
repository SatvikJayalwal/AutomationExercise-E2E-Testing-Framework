# API 6: POST To Search Product without search_product parameter
# API URL: https://automationexercise.com/api/searchProduct
# Request Method: POST
# Expected Response Code: 400
# Expected Response Message: "Bad request, search_product parameter is missing in POST request."

import requests
import json

# API URL
url = "https://automationexercise.com/api/searchProduct"

# Payload (empty on purpose to trigger error)
payload = {}

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

# Validate response message
assert "search_product parameter is missing" in response_text, "Unexpected response message!"