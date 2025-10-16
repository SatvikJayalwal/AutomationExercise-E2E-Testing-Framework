"""
Signup page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.logger import logger


class SignupPage(BasePage):
    """Signup page class containing locators and methods for the signup page."""
    
    # Account information locators
    ACCOUNT_INFO_FORM = (By.XPATH, "//div[@class='login-form']")
    GENDER_MR = (By.XPATH, "//input[@id='id_gender1']")
    GENDER_MRS = (By.XPATH, "//input[@id='id_gender2']")
    PASSWORD = (By.XPATH, "//input[@data-qa='password']")
    DAYS_DROPDOWN = (By.XPATH, "//select[@id='days']")
    MONTHS_DROPDOWN = (By.XPATH, "//select[@id='months']")
    YEARS_DROPDOWN = (By.XPATH, "//select[@id='years']")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//input[@id='newsletter']")
    OPTIN_CHECKBOX = (By.XPATH, "//input[@id='optin']")
    
    # Address information locators
    FIRST_NAME = (By.XPATH, "//input[@id='first_name']")
    LAST_NAME = (By.XPATH, "//input[@id='last_name']")
    COMPANY = (By.XPATH, "//input[@id='company']")
    ADDRESS1 = (By.XPATH, "//input[@id='address1']")
    ADDRESS2 = (By.XPATH, "//input[@id='address2']")
    COUNTRY_DROPDOWN = (By.XPATH, "//select[@id='country']")
    STATE = (By.XPATH, "//input[@id='state']")
    CITY = (By.XPATH, "//input[@id='city']")
    ZIPCODE = (By.XPATH, "//input[@id='zipcode']")
    MOBILE_NUMBER = (By.XPATH, "//input[@id='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    
    # Success/Error messages
    ACCOUNT_CREATED_MESSAGE = (By.XPATH, "//div[@class='container']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_account_info_form_visible(self) -> bool:
        """Check if account information form is visible."""
        return self.helper.is_element_displayed(self.ACCOUNT_INFO_FORM)
    
    def select_gender(self, gender: str) -> bool:
        """Select gender (Mr or Mrs)."""
        try:
            if gender.lower() == "mr":
                return self.helper.click_element(self.GENDER_MR)
            elif gender.lower() == "mrs":
                return self.helper.click_element(self.GENDER_MRS)
            else:
                logger.error(f"Invalid gender: {gender}")
                return False
        except Exception as e:
            logger.error(f"Failed to select gender: {e}")
            return False
    
    def enter_password(self, password: str) -> bool:
        """Enter password."""
        return self.helper.send_keys_to_element(self.PASSWORD, password)
    
    def select_date_of_birth(self, day: str, month: str, year: str) -> bool:
        """Select date of birth."""
        try:
            # Select day
            if not self.helper.select_dropdown_by_text(self.DAYS_DROPDOWN, day):
                return False
            
            # Select month
            if not self.helper.select_dropdown_by_text(self.MONTHS_DROPDOWN, month):
                return False
            
            # Select year
            if not self.helper.select_dropdown_by_text(self.YEARS_DROPDOWN, year):
                return False
            
            logger.info(f"Selected date of birth: {day} {month} {year}")
            return True
        except Exception as e:
            logger.error(f"Failed to select date of birth: {e}")
            return False
    
    def select_newsletter(self) -> bool:
        """Select newsletter checkbox."""
        return self.helper.click_element(self.NEWSLETTER_CHECKBOX)
    
    def select_optin(self) -> bool:
        """Select optin checkbox."""
        return self.helper.click_element(self.OPTIN_CHECKBOX)
    
    def enter_address_info(self, first_name: str, last_name: str, company: str, 
                          address1: str, address2: str = "", country: str = "", 
                          state: str = "", city: str = "", zipcode: str = "", 
                          mobile_number: str = "") -> bool:
        """Enter address information."""
        try:
            # Enter first name
            if not self.helper.send_keys_to_element(self.FIRST_NAME, first_name):
                return False
            
            # Enter last name
            if not self.helper.send_keys_to_element(self.LAST_NAME, last_name):
                return False
            
            # Enter company
            if company and not self.helper.send_keys_to_element(self.COMPANY, company):
                return False
            
            # Enter address1
            if not self.helper.send_keys_to_element(self.ADDRESS1, address1):
                return False
            
            # Enter address2 (optional)
            if address2 and not self.helper.send_keys_to_element(self.ADDRESS2, address2):
                return False
            
            # Select country
            if country and not self.helper.select_dropdown_by_text(self.COUNTRY_DROPDOWN, country):
                return False
            
            # Enter state
            if state and not self.helper.send_keys_to_element(self.STATE, state):
                return False
            
            # Enter city
            if city and not self.helper.send_keys_to_element(self.CITY, city):
                return False
            
            # Enter zipcode
            if zipcode and not self.helper.send_keys_to_element(self.ZIPCODE, zipcode):
                return False
            
            # Enter mobile number
            if mobile_number and not self.helper.send_keys_to_element(self.MOBILE_NUMBER, mobile_number):
                return False
            
            logger.info("Entered address information")
            return True
        except Exception as e:
            logger.error(f"Failed to enter address information: {e}")
            return False
    
    def create_account(self) -> bool:
        """Click create account button."""
        return self.helper.click_element(self.CREATE_ACCOUNT_BUTTON)
    
    def is_account_created(self) -> bool:
        """Check if account created message is visible."""
        return self.helper.is_element_displayed(self.ACCOUNT_CREATED_MESSAGE)
    
    def get_account_created_message(self) -> str:
        """Get the account created message."""
        return self.helper.get_element_text(self.ACCOUNT_CREATED_MESSAGE)
    
    def click_continue(self) -> bool:
        """Click continue button."""
        return self.helper.click_element(self.CONTINUE_BUTTON)
    
    def complete_signup(self, user_data: dict) -> bool:
        """Complete the entire signup process."""
        try:
            # Select gender
            if not self.select_gender(user_data.get('title', 'Mr')):
                return False
            
            # Enter password
            if not self.enter_password(user_data.get('password', '')):
                return False
            
            # Select date of birth
            if not self.select_date_of_birth(
                user_data.get('day', '15'),
                user_data.get('month', 'November'),
                user_data.get('year', '1990')
            ):
                return False
            
            # Select newsletter and optin
            self.select_newsletter()
            self.select_optin()
            
            # Enter address information
            if not self.enter_address_info(
                user_data.get('first_name', ''),
                user_data.get('last_name', ''),
                user_data.get('company', ''),
                user_data.get('address1', ''),
                user_data.get('address2', ''),
                user_data.get('country', ''),
                user_data.get('state', ''),
                user_data.get('city', ''),
                user_data.get('zipcode', ''),
                user_data.get('mobile_number', '')
            ):
                return False
            
            # Create account
            if not self.create_account():
                return False
            
            logger.info("Completed signup process")
            return True
        except Exception as e:
            logger.error(f"Failed to complete signup: {e}")
            return False
