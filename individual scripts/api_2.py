# API 2: POST To All Products List
# API URL: https://automationexercise.com/api/productsList
# Request Method: POST
# Expected Response Code: 405 (but API actually gives 200)
# Expected Response Message: "This request method is not supported."

import requests 
import json

# API URL
url = "https://automationexercise.com/api/productsList"

# Send POST request (wrong method on purpose)
response = requests.post(url)

# Capture status code
status = response.status_code
print("Status Code:", status)

# Expected 405 but actual is 200 -> Log bug
if status != 405:
    print(f"[BUG] Expected 405 (Method Not Allowed), but got {status}")
else:
    print("Status code is correct (405)")

# Print response text from server
response_text = response.text
print("Response text:", response_text)

# If 405 as expected, validate error message
if status == 405:
    assert "This request method is not supported" in response_text, "Unexpected response message!"
