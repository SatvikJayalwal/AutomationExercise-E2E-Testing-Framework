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

# Click 'Products' button
driver.find_element(By.XPATH, "//a[@href='/products']").click()

# Veriy Products page is displayed
products_title = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'All Products')]"))
)
assert products_title.is_displayed(), "PRODUCTS TITLE not displayed"

# Add products to cart
product_31 = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='31']"))
)
product_31.click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

product_35 = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='35']"))
)
product_35.click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

product_43 = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='43']"))
)
product_43.click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

# Click 'Cart' button
view_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/view_cart']"))
)
view_cart.click()

# Verify that cart page is displayed
cart_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@class='btn btn-default check_out']"))
)
assert cart_page.is_displayed(), "CART PAGE not displayed"

# Click 'X' button corresponding to particular product
""" 

NOTE:

The Automation Exercise website previously had an 'X' (delete) button in the cart 
to remove individual products. 
As of now (checked in September 2025), this option has been removed from the UI. 
Therefore, the "remove product from cart" test case is skipped.
Verify that product is removed from the cart 

"""

# Quit driver
time.sleep(2)
driver.quit()
