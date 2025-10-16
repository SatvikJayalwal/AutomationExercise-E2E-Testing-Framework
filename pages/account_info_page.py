"""
Account info page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class AccountInfoPage(BasePage):
    """Account info page class containing locators and methods for account information."""
    
    # Account info locators
    ACCOUNT_DELETED_MESSAGE = (By.XPATH, "//h2[@data-qa='account-deleted']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_account_deleted_message_visible(self) -> bool:
        """Check if account deleted message is visible."""
        return self.helper.is_element_displayed(self.ACCOUNT_DELETED_MESSAGE)
    
    def get_account_deleted_message(self) -> str:
        """Get the account deleted message."""
        return self.helper.get_element_text(self.ACCOUNT_DELETED_MESSAGE)
    
    def click_continue(self) -> bool:
        """Click continue button."""
        return self.helper.click_element(self.CONTINUE_BUTTON)
    
    def verify_account_deletion(self) -> bool:
        """Verify that account deletion was successful."""
        try:
            if self.is_account_deleted_message_visible():
                message = self.get_account_deleted_message()
                if "ACCOUNT DELETED!" in message:
                    logger.info("Account deletion confirmed")
                    return True
                else:
                    logger.error(f"Unexpected account deletion message: {message}")
                    return False
            else:
                logger.error("Account deletion message not visible")
                return False
        except Exception as e:
            logger.error(f"Failed to verify account deletion: {e}")
            return False
