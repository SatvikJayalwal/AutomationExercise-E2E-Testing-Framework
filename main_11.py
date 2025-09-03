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

# Click 'Cart' button
driver.find_element(By.XPATH,"//a[@href='/view_cart']").click()

# Scroll down to footer
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//"))
)
# Verify text 'SUBSCRIPTION'
# Enter email address in input and click arrow button
# Verify success message 'You have been successfully subscribed!' is visible