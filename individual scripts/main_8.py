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
products_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']"))
)
assert products_page.is_displayed(), "ALL PRODUCTS PAGE not displayed"

# The products list is visible
product_list = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@href='/product_details/1']"))
)
assert product_list.is_displayed(), "PRODUCT LIST not displayed"

# Click on 'View Product' of first product
driver.find_element(By.XPATH,"//a[@href='/product_details/1']").click()

# User is landed to product detail page
product_detail = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//img[@alt='ecommerce website products']"))
)
assert product_detail.is_displayed(), "PRODUCT LIST not displayed"

# Verify that detail is visible: product name, category, price, availability, condition, brand
product_detail_visible_verify = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='product-information']"))
)
assert product_detail_visible_verify.is_displayed(), "DETAILS not displayed"

# Quit driver
time.sleep(2)
driver.quit()