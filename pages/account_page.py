from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    # Locators for account verification and deletion
    account_created_text = (By.XPATH, "//div[@class='container']")
    continue_btn = (By.XPATH, "//a[@data-qa='continue-button']")
    logged_in_text = (By.XPATH, "//li[contains(.,'Logged in as')]")
    delete_account_btn = (By.XPATH, "//a[@href='/delete_account']")
    account_deleted_text = (By.XPATH, "//h2[@data-qa='account-deleted']")

    # Verify account created
    def verify_account_created(self):
        element = self.find_element(self.account_created_text)
        assert "ACCOUNT CREATED!" in element.text

    # Click continue after account creation
    def continue_after_creation(self):
        self.click(self.continue_btn)

    # Verify logged in username
    def verify_logged_in_user(self, username):
        element = self.find_element(self.logged_in_text)
        assert element.is_displayed()
        assert username in element.text

    # Delete account
    def delete_account(self):
        self.click(self.delete_account_btn)

    # Verify account deleted
    def verify_account_deleted(self):
        element = self.find_element(self.account_deleted_text)
        assert "ACCOUNT DELETED!" in element.text

    # Continue after deletion
    def continue_after_deletion(self):
        self.click(self.continue_btn)
