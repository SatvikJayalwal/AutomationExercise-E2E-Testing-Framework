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

# Click on 'View Product' button
view_product = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/product_details/21']"))
)
view_product.click()

# Verify 'Write Your Review' is visible
write_your_review = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//a[@href='#reviews']"))
)
write_your_review.is_displayed(), "WRITE YOUR REVIEW not displayed"

# Enter name, email and review
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Satvik Jayalwal")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("satvikjayalwalips@gmail.com")
driver.find_element(By.XPATH,"//textarea[@id='review']").send_keys("Test Review...")

# Click 'Submit' button
driver.find_element(By.XPATH,"//button[@id='button-review']").send_keys("Test Review...")

# Verify success message 'Thank you for your review.'
success_msg = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='alert-success alert' and contains(normalize-space(), 'Thank you for your review.')]"))
)
assert success_msg.is_displayed(), "THANK YOU FOR YOUR REVIEW. not visible"

# Quit driver
time.sleep(2)
driver.quit()
