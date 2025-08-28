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
assert home_logo.is_displayed, "HOME PAGE not displayed"

# Click on 'Signup / Login' button
driver.find_element(By.XPATH,"//a[@href='/login']").click()

# Verify 'New User Signup!' is visible
signup = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='signup-form']"))
)
assert signup.is_displayed(), "NEW USER SIGNUP! not displayed"

# Enter name and already registered email address
driver.find_element(By.XPATH,"//input[@data-qa='signup-name']").send_keys("Satvik Jayalwal")
driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("satvikjayalwalips@gmail.com")

# Click 'Signup' button
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()

# Verify error 'Email Address already exist!' is visible
email_already_exist = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Email Address already exist!']"))
)
assert email_already_exist.is_displayed(), "EMAIL ADDRESS ALREADY EXIST!" 

# Quit driver
time.sleep(2)
driver.quit()