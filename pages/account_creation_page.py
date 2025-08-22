from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountCreationPage(BasePage):
    # Locators for account creation form
    title_male = (By.XPATH, "//input[@id='id_gender1']")
    password_input = (By.XPATH, "//input[@data-qa='password']")
    days_select = (By.XPATH, "//select[@id='days']")
    months_select = (By.XPATH, "//select[@id='months']")
    years_select = (By.XPATH, "//select[@id='years']")
    newsletter_checkbox = (By.XPATH, "//input[@id='newsletter']")
    offers_checkbox = (By.XPATH, "//input[@id='optin']")
    first_name_input = (By.XPATH, "//input[@id='first_name']")
    last_name_input = (By.XPATH, "//input[@id='last_name']")
    company_input = (By.XPATH, "//input[@id='company']")
    address1_input = (By.XPATH, "//input[@id='address1']")
    country_select = (By.XPATH, "//select[@id='country']")
    state_input = (By.XPATH, "//input[@id='state']")
    city_input = (By.XPATH, "//input[@id='city']")
    zipcode_input = (By.XPATH, "//input[@id='zipcode']")
    mobile_input = (By.XPATH, "//input[@id='mobile_number']")
    create_account_btn = (By.XPATH, "//button[@data-qa='create-account']")

    # Fill all account info
    def fill_account_info(self, user):
        self.click(self.title_male)  # Select gender
        self.send_keys(self.password_input, user['password'])
        self.select_by_visible_text(self.days_select, user['dob']['day'])
        self.select_by_visible_text(self.months_select, user['dob']['month'])
        self.select_by_visible_text(self.years_select, user['dob']['year'])
        self.click(self.newsletter_checkbox)  # Subscribe newsletter
        self.click(self.offers_checkbox)      # Receive offers
        self.send_keys(self.first_name_input, user['first_name'])
        self.send_keys(self.last_name_input, user['last_name'])
        self.send_keys(self.company_input, user['company'])
        self.send_keys(self.address1_input, user['address1'])
        self.select_by_visible_text(self.country_select, user['country'])
        self.send_keys(self.state_input, user['state'])
        self.send_keys(self.city_input, user['city'])
        self.send_keys(self.zipcode_input, user['zipcode'])
        self.send_keys(self.mobile_input, user['mobile_number'])

    # Click create account button
    def create_account(self):
        self.click(self.create_account_btn)
