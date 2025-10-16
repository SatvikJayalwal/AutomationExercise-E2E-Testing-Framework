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

# Go to products tab
driver.find_element(By.XPATH,"//a[@href='/products']").click()

# Verify user is navigated to ALL PRODUCTS page successfully
product_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']"))
)
assert product_page.is_displayed(), "PRODUCT PAGE not displayed"

# Click 'View Product' for any product on home page
product_12 = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/product_details/12']"))
)
product_12.click()

product_12_name = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='product-information']/h2"))
)
product_12_name_text = product_12_name.text

# Verify product detail is opened
product_detail_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//button[@class='btn btn-default cart']"))
)

# Increase quantity to 4
quantity = driver.find_element(By.XPATH,"//input[@id='quantity']")
quantity.clear()
quantity_number = 4
quantity.send_keys(quantity_number)

# Click 'Add to cart' button
add_to_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-default cart']"))
)
add_to_cart.click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

# Click 'View Cart' button
view_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/view_cart']"))
)
view_cart.click()

# Verify that Cart page is loaded successfully
cart_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@class='btn btn-default check_out']"))
)
assert cart_page.is_displayed(), "CART PAGE not displayed"

# Locate the <a> element with product name inside cart
cart_product_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, f"//td[@class='cart_description']/h4/a[normalize-space(text())='{product_12_name_text}']")
    )
)

# Extract product name text
cart_product_name = cart_product_element.text.strip()

# Go up to <tr> (the full row of that product)
cart_row = cart_product_element.find_element(By.XPATH, "./ancestor::tr")

# From the row, get the quantity value
cart_quantity = cart_row.find_element(By.XPATH, ".//td[@class='cart_quantity']/button").text.strip()

# Assertions
assert cart_product_name == product_12_name_text, f"Expected product '{product_12_name_text}', but got '{cart_product_name}'"
assert cart_quantity == str(quantity_number), f"Expected quantity '{quantity_number}', but got '{cart_quantity}'"

# Quit driver
time.sleep(2)
driver.quit()



