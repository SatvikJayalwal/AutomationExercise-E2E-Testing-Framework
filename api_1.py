# API 1: Get All Products List

import requests
import json

# API URL
url = "https://automationexercise.com/api/productsList"

# Send GET request
response = requests.get(url)

# Validate Status Code
status = response.status_code
print(f"Status Code : {status}")
assert status == 200, f"Expected 200(OK) but got {status}"

# Parse JSON response
data = response.json()

# Print data 
print(json.dumps(data,indent=2))

# Validate 'products' key exits 
assert "products" in data, "'products' key not found in response"

# Validate product list is not empty 
assert len(data['products']) > 0, "Product list is empty"