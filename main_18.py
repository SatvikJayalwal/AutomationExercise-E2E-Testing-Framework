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

# Verify that categories are visible on left side bar
category = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='left-sidebar']/h2"))
)
assert category.is_displayed(), "CATEGORY not displayed"

# Click on 'Women' category
women = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='#Women']"))
)
women.click()

# Click on any category link under 'Women' category, for example: Tops
women_tops = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/category_products/2']"))
)
women_tops.click()

# Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
tops_products = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']//h2[contains(normalize-space(),'Women - Tops Products')]"))
)
assert tops_products.is_displayed(), "WOMEN - TOPS PRODUCTS not displayed"

# Click on 'Men' category
men = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='#Men']"))
)
men.click()

# Click on any category link under 'Men' category, for example: Jeans
men_tops = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/category_products/6']"))
)
men_tops.click()

# Verify that user is navigated to that category page
jeans_products = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='features_items']//h2[contains(normalize-space(),'Men - Jeans Products')]"))
)
assert jeans_products.is_displayed(), "MEN - JEANS PRODUCTS not displayed"

# Quit driver
time.sleep(2)
driver.quit()