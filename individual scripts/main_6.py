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

# Click on 'Contact Us' button
driver.find_element(By.XPATH,"//a[@href='/contact_us']").click()

# Verify 'GET IN TOUCH' is visible
get_in_touch = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Get In Touch']")) 
)
assert get_in_touch.is_displayed(), "GET IN TOUCH not displayed"

# Enter name, email, subject and message
driver.find_element(By.XPATH,"//input[@data-qa='name']").send_keys("Satvik Jayalwal")
driver.find_element(By.XPATH,"//input[@data-qa='email']").send_keys("satvikjayalwalips@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='subject']").send_keys("Testing the website")
driver.find_element(By.XPATH,"//textarea[@data-qa='message']").send_keys("This is a test message")

# Upload file
driver.find_element(By.XPATH,"//input[@name='upload_file']").send_keys("C:\\Users\\HP\\OneDrive\\Desktop\\Test files\\Test file.pdf")

# Click 'Submit' button
driver.find_element(By.XPATH,"//input[@data-qa='submit-button']").click()

# Click OK button
WebDriverWait(driver,10).until(
    EC.alert_is_present()
)
alert = driver.switch_to.alert
alert.accept()

# Verify success message 'Success! Your details have been submitted successfully.' is visible
success_msg = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[normalize-space()='Success! Your details have been submitted successfully.']"))
)
assert success_msg.is_displayed(), "SUCCESS! YOUR DETAILS HAVE BEEN SUBMITTED SUCCESSFULLY. is not displayed"

# Click 'Home' button 
home_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-success']"))
)
home_btn.click()

# Verify that landed to home page successfully
home_logo = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//img[@alt='Website for automation practice']"))
)

assert home_logo.is_displayed(), "HOME PAGE not displayed"

# Quit driver
time.sleep(2)
driver.quit() 