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

#Click on 'Signup / Login' button
driver.find_element(By.XPATH,"//a[@href='/login']").click()

# Verify 'New User Signup!' is visible

signup=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='signup-form']"))
)
assert signup.is_displayed(), "NEW USER SIGNUP FORM is not visible"

# Enter name and email address
driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("Satvik Jayalwal")
driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("satvikjayalwalips@gmail.com")

# Click 'Signup' button
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()

# Verify that 'ENTER ACCOUNT INFORMATION' is visible
account_info=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='login-form']"))
)
assert account_info.is_displayed(), "ENTER ACCOUNT INFORMATION is not visible"

# Fill details: Title, Name, Email, Password, Date of birth
gender=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//input[@id='id_gender1']"))
)
gender.click()
# NOTE (Name and email is already fetched so not need to fill it)
driver.find_element(By.XPATH,"//input[@data-qa='password']").send_keys("123456")
Select(driver.find_element(By.XPATH,"//select[@id='days']")).select_by_visible_text("15")
Select(driver.find_element(By.XPATH,"//select[@id='months']")).select_by_visible_text("November")
Select(driver.find_element(By.XPATH,"//select[@id='years']")).select_by_visible_text("2004")

# Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.XPATH,"//input[@id='newsletter']").click()

# Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.XPATH,"//input[@id='optin']").click()

# Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Satvik")
driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("Jayalwal")
driver.find_element(By.XPATH,"//input[@id='company']").send_keys("Satvik Solutions Pvt. Ltd.")
driver.find_element(By.XPATH,"//input[@id='address1']").send_keys("Sector-47, Gurugram, Haryana, India")
Select(driver.find_element(By.XPATH,"//select[@id='country']")).select_by_visible_text("India")
driver.find_element(By.XPATH,"//input[@id='state']").send_keys("Haryana")
driver.find_element(By.XPATH,"//input[@id='city']").send_keys("Gurugram")
driver.find_element(By.XPATH,"//input[@id='zipcode']").send_keys("122001")
driver.find_element(By.XPATH,"//input[@id='mobile_number']").send_keys("8810655751")

# Click 'Create Account button'
driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()

# Verify that 'ACCOUNT CREATED!' is visible
account_created=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='container']"))
)
assert account_created.is_displayed(), "ACCOUNT CREATED! is not visible"

# Click 'Continue' button
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()

# Verify that 'Logged in as username' is visible
logged_in=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//li[contains(.,'Logged in as')]"))
)
assert logged_in.is_displayed(), "Logged in as username not visible"
assert "Satvik Jayalwal" in logged_in.text, "Correct username not visible"

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
