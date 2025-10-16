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

# Click on 'Test Cases' button
driver.find_element(By.XPATH,"//a[@href='/test_cases']").click()

# Verify user is navigated to test cases page successfully
test_cases_page = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//b[normalize-space()='Test Cases']"))
)
assert test_cases_page.is_displayed(), "TEST CASES PAGE not displayed"

# Quit driver
time.sleep(2)
driver.quit()