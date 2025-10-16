import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Launch browser
driver = webdriver.Chrome()

# Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")

# Verify that home page is visible successfully
home_logo = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//img[@alt='Website for automation practice']"))
)
assert home_logo.is_displayed(), "HOME PAGE not displayed"

# Click on 'Products' button
driver.find_element(By.XPATH,"//a[@href='/products']").click()

# Verify user is navigated to ALL PRODUCTS page successfully
product_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']"))
)
assert product_page.is_displayed(), "PRODUCT PAGE not displayed"

# Enter product name in search input and click search button
product = "Premium Polo T-Shirts"
search_product = driver.find_element(By.XPATH,"//input[@id='search_product']").send_keys(product)
search_button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@id='submit_search']"))
)
search_button.click()

# Verify 'SEARCHED PRODUCTS' is visible
searched_products = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Searched Products']"))
)
assert searched_products.is_displayed(), "SEARCHED PRODUCTS not displayed" 

# Verify all the products related to search are visible
# Step 8: Verify all products related to search are visible
products = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")

# Check if each product contains the search term
for p in products:
    product_name = p.text
    assert product.lower() in product_name.lower(), f"Product '{product_name}' does not match search '{product}'"

# Quit driver
time.sleep(2)
driver.quit()

