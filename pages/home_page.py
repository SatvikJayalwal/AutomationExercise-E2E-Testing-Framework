from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    logo = (By.XPATH, "//img[@alt='Website for automation practice']")
    signup_login_btn = (By.XPATH, "//a[@href='/login']")

    # Verify home page is visible
    def verify_home_page(self):
        assert self.find_element(self.logo).is_displayed(), "HOME PAGE not visible"

    # Navigate to signup/login page
    def go_to_signup_login(self):
        self.click(self.signup_login_btn)
