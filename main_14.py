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

# Click 'Cart' button
# Verify that cart page is displayed
# Click Proceed To Checkout
# Click 'Register / Login' button
# Fill all details in Signup and create account
# Verify 'ACCOUNT CREATED!' and click 'Continue' button
# Verify ' Logged in as username' at top
# Click 'Cart' button
# Click 'Proceed To Checkout' button
# Verify Address Details and Review Your Order
# Enter description in comment text area and click 'Place Order'
# Enter payment details: Name on Card, Card Number, CVC, Expiration date
# Click 'Pay and Confirm Order' button
# Verify success message 'Your order has been placed successfully!'
# Click 'Delete Account' button
# Verify 'ACCOUNT DELETED!' and click 'Continue' button