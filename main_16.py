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

# Click on 'Signup / Login' button
driver.find_element(By.XPATH,"//a[@href='/login']").click()

# Verify 'Login to your account' is visible
login = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='login-form']"))
)
assert login.is_displayed(), "LOGIN TO YOUR ACCOUNT is not visible"

# Enter correct email address and password
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("satvikjayalwalips@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("123456")

# Click 'login' button
driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()

# Verify that 'Logged in as username' is visible
logged_in = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//li[contains(.,'Logged in as')]"))
)
assert logged_in.is_displayed(), "LOGGED IN AS USERNAME not displayed"
assert "Satvik Jayalwal" in logged_in.text, "Correct username not displayed"

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

# Click Proceed To Checkout
proceed_to_checkout = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-default check_out']"))
)
proceed_to_checkout.click()

# Verify Address Details 

delivery_address_details = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//ul[@id='address_delivery']"))
)
assert delivery_address_details.is_displayed(), "DELIVERY ADDRESS DETAILS not displayed"

billing_address_details = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//ul[@id='address_delivery']"))
)
assert billing_address_details.is_displayed(), "BILLING ADDRESS DETAILS not displayed"

assert delivery_address_details.text.strip() == billing_address_details.text.strip(), "INCORRECT ADDRESS DETAILS"

# Review Your Order
review_product_31 = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@href='/product_details/31']"))
)
assert "Pure Cotton Neon Green Tshirt" in review_product_31.text.strip()

review_product_35 = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@href='/product_details/35']"))
)
assert "Regular Fit Straight Jeans" in review_product_35.text.strip()

review_product_43 = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@href='/product_details/43']"))
)
assert "GRAPHIC DESIGN MEN T SHIRT - BLUE" in review_product_43.text.strip()

# Enter description in comment text area and click 'Place Order'
driver.find_element(By.XPATH,"//textarea[@class='form-control']").send_keys("Test description...")

place_order = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/payment']"))
)
place_order.click()

# Verify payment page is loaded
payment_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='step-one']/h2"))
)
assert payment_page.is_displayed(), "PAYMENT PAGE not displayed"

# Enter Name on Card
driver.find_element(By.XPATH,"//input[@data-qa='name-on-card']").send_keys("Satvik Jayalwal")
# Enter Card Number
driver.find_element(By.XPATH,"//input[@data-qa='card-number']").send_keys("123456789")
# Enter CVC
driver.find_element(By.XPATH,"//input[@data-qa='cvc']").send_keys("069")
# Enter Expiration MM
driver.find_element(By.XPATH,"//input[@data-qa='expiry-month']").send_keys("11")
# Enter Expiration YYYY
driver.find_element(By.XPATH,"//input[@data-qa='expiry-year']").send_keys("2060")

# Click 'Pay and Confirm Order' button
pay_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='pay-button']"))
)
pay_btn.click()

# Verify success message 'Your order has been placed successfully!'
order_placed = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//h2[@data-qa='order-placed']"))
)
assert "ORDER PLACED!" in order_placed.text.strip()

# Click 'Continue' button
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()

# Click 'Delete Account' button
driver.find_element(By.XPATH,"//a[@href='/delete_account']").click()

# Verify that 'ACCOUNT DELETED!' is visible  
account_deleted=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//h2[@data-qa='account-deleted']"))
)
assert "ACCOUNT DELETED!" in account_deleted.text, "ACCOUNT DELETED! is not visible"

# Click 'Continue' button
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()

# Quit driver
time.sleep(2)
driver.quit()










 











