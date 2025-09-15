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

# Verify that Brands are visible on left side bar
brands = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='brands_products']"))
)
assert brands.is_displayed(), "BRANDS not displayed"

# Click on any brand name
brand_1_click= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/brand_products/H&M']"))
)
brand_1_click.click()

# Verify that user is navigated to brand page and brand products are displayed
brand_1_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']//h2[contains(normalize-space(),'Brand - H&M Products')]"))
)
assert brand_1_page.is_displayed(), "BRAND PAGE not displayed"

# On left side bar, click on any other brand link
brand_2_click= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/brand_products/Polo']"))
)
brand_2_click.click()

# Verify that user is navigated to that brand page and can see products
brand_2_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']//h2[contains(normalize-space(),'Brand - Polo Products')]"))
)
assert brand_2_page.is_displayed(), "BRAND PAGE not displayed"

# Quit driver
time.sleep(2)
driver.quit()