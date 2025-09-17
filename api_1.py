# API 1: Get All Products List
# API URL: https://automationexercise.com/api/productsList
# Request Method: GET
# Response Code: 200
# Response JSON: All products list

import requests
import json

# API URL
url = "https://automationexercise.com/api/productsList"

# Send GET request
response = requests.get(url)

# Capture Status Code
status = response.status_code
print(f"Status Code : {status}")

# Assert expected status code
assert status == 200, f"Expected 200(OK) but got {status}"

# Parse JSON response
data = response.json()

# Print data 
print(json.dumps(data,indent=2))

# Validate 'products' key exits 
assert "products" in data, "'products' key not found in response"

# Validate product list is not empty 
assert len(data['products']) > 0, "Product list is empty"