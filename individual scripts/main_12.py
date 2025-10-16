import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")

# Verify that home page is visible successfully
home_logo = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//img[@alt='Website for automation practice']"))
)
assert home_logo.is_displayed(), "HOME PAGE not visible"

# Click 'Products' button
driver.find_element(By.XPATH, "//a[@href='/products']").click()

products_title = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'All Products')]"))
)
assert products_title.is_displayed(), "PRODUCTS TITLE not displayed"

# Get product names before adding
first_product_name = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center']/p)[1]").text
second_product_name = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center']/p)[2]").text

# Add first product
product_1 = driver.find_element(By.XPATH, "(//a[@data-product-id='1'])[1]").click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

# Add second product
product_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//a[@data-product-id='2'])[1]"))
)
product_2.click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

# Go to Cart
click_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']"))
)
click_cart.click()

# Verify Cart page is loaded
cart_page = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='cart_info']"))
)
assert cart_page.is_displayed(), "Cart page not visible"

# Verify products in Cart
cart_products = driver.find_elements(By.XPATH, "//td[@class='cart_description']/h4/a")
cart_product_names = [prod.text for prod in cart_products]

assert first_product_name in cart_product_names, f"{first_product_name} not found in cart"
assert second_product_name in cart_product_names, f"{second_product_name} not found in cart"

# Verify Price, Quantity, Total
cart_rows = driver.find_elements(By.XPATH, "//tr[contains(@id,'product-')]")

for row in cart_rows:
    product_name = row.find_element(By.XPATH, ".//h4/a").text
    price = row.find_element(By.XPATH, ".//td[@class='cart_price']/p").text
    quantity = row.find_element(By.XPATH, ".//button[@class='disabled']").text
    total = row.find_element(By.XPATH, ".//p[@class='cart_total_price']").text

    assert int(quantity) >= 1, f"Quantity invalid for {product_name}"
    assert total.startswith("Rs."), f"Total format invalid for {product_name}"


# Quit driver
time.sleep(2)
driver.quit()
