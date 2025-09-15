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

# Enter product name in search input and click search button
driver.find_element(By.XPATH,"//input[@id='search_product']").send_keys("Full Sleeves Top Cherry - Pink")
search_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@id='submit_search']"))
)
search_btn.click()

# Verify 'SEARCHED PRODUCT' is visible
searched_products = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='productinfo text-center']//p"))
)
assert "Full Sleeves Top Cherry - Pink" in searched_products.text.strip(), "SEARCHED PRODUCT not displayed"

# Add those products to cart
add_to_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//div[@class='productinfo text-center']//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart']"))
)
add_to_cart.click()

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

# Again, go to Cart page
view_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/view_cart']"))
)
view_cart.click()

# Verify that cart page is displayed
cart_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@class='btn btn-default check_out']"))
)
assert cart_page.is_displayed(), "CART PAGE not displayed"

# Verify that those products are visible in cart after login as well
cart_description = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//td[@class='cart_description']//a[@href='/product_details/14']"))
)
assert 	"Full Sleeves Top Cherry - Pink" in cart_description.text.strip()

# Quit driver
time.sleep(2)
driver.quit()