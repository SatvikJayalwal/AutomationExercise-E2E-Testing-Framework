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
subscription = driver.find_element(By.XPATH,"//div[@class='single-widget']/h2")
driver.execute_script("arguments[0].scrollIntoView();", subscription)

# Verify text 'SUBSCRIPTION'
assert "SUBSCRIPTION"==subscription.text

# Enter email address in input and click arrow button
email = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//input[@id='susbscribe_email']"))
)
email.send_keys("satvikjayalwalips@gmail.com")

arrow = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@id='subscribe']"))
)
arrow.click()       

# Verify success message 'You have been successfully subscribed!' is visible
subscribe_success_msg = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='alert-success alert']"))
)

assert subscribe_success_msg.is_displayed(), "YOU HAVE BEEN SUCCESSFULLY SUBSCRIBED not visible"

# Quit driver
time.sleep(2)
driver.quit()