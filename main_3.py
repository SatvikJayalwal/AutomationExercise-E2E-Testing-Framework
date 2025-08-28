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
assert home_logo.is_displayed, "HOME PAGE is not displayed"

# Click on 'Signup / Login' button
driver.find_element(By.XPATH,"//a[@href='/login']").click()

# Verify 'Login to your account' is visible
logged_in = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='login-form']"))
)
assert logged_in.is_displayed(), "LOGIN TO YOUR ACCOUNT is not displayed"

# Enter incorrect email address and password
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("incorrect_test@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("123")

# Click 'login' button
driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()

# Verify error 'Your email or password is incorrect!' is visible
incorrect_msg = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']"))
)
assert incorrect_msg.is_displayed(), "YOUR EMAIL OR PASSWORD IS INCORRECT! is not displayed"