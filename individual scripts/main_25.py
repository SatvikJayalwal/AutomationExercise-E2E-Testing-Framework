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

# Scroll down to footer
subscription = driver.find_element(By.XPATH,"//div[@class='single-widget']/h2")
driver.execute_script("arguments[0].scrollIntoView();", subscription)

# Verify text 'SUBSCRIPTION'
assert "SUBSCRIPTION"==subscription.text

# Click on arrow at bottom right side to move upward
click_arrow = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@id='scrollUp']"))
)
click_arrow.click()

# Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
home_logo = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//img[@alt='Website for automation practice']"))
)
assert home_logo.is_displayed(), "HOME Logo not displayed"

# Quit driver
time.sleep(2)
driver.quit()