from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    # Locators
    signup_form = (By.XPATH, "//div[@class='signup-form']")
    name_input = (By.XPATH, "//input[@placeholder='Name']")
    email_input = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

    # Verify signup form is visible
    def verify_signup_form(self):
        assert self.find_element(self.signup_form).is_displayed(), "Signup form not visible"

    # Enter signup details
    def enter_signup_details(self, name, email):
        self.send_keys(self.name_input, name)
        self.send_keys(self.email_input, email)

    # Click signup button
    def click_signup(self):
        self.click(self.signup_btn)
