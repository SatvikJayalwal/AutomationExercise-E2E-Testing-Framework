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

# Scroll to bottom of page
# Verify 'RECOMMENDED ITEMS' are visible
recommended_items = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='recommended_items']//h2[normalize-space()='recommended items']"))
)
assert recommended_items.is_displayed(), "RECOMMENDED ITEMS not displayed"

# Click on 'Add To Cart' on Recommended product
add_to_cart = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[74]"))
)
add_to_cart.click()

# Click 'Continue Shopping' button
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
)
continue_button.click()

# Click on 'View Cart' button
view_cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/view_cart']"))
)
view_cart.click()

# Verify that product is displayed in cart page
product_description = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@href='/product_details/6']"))
)
assert "Summer White Top" in product_description.text.strip(), "PRODUCT not displayed in cart page"

# Quit driver
time.sleep(2)
driver.quit()

