"""
Home page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class HomePage(BasePage):
    """Home page class containing locators and methods for the home page."""
    
    # Home page specific locators
    SUBSCRIPTION_HEADER = (By.XPATH, "//div[@class='single-widget']/h2")
    SUBSCRIPTION_EMAIL = (By.XPATH, "//input[@id='susbscribe_email']")
    SUBSCRIPTION_BUTTON = (By.XPATH, "//button[@id='subscribe']")
    SUBSCRIPTION_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert-success alert']")
    FEATURES_ITEMS = (By.XPATH, "//div[@class='features_items']")
    RECOMMENDED_ITEMS = (By.XPATH, "//div[@class='recommended_items']")
    CATEGORY_WOMEN = (By.XPATH, "//a[@href='#Women']")
    CATEGORY_MEN = (By.XPATH, "//a[@href='#Men']")
    CATEGORY_KIDS = (By.XPATH, "//a[@href='#Kids']")
    TEST_CASES_BUTTON = (By.XPATH, "//a[@href='/test_cases']")
    TEST_CASES_HEADER = (By.XPATH, "//b[normalize-space()='Test Cases']")
    TEST_CASES_CONTENT = (By.XPATH, "//div[@class='container']")
    CATEGORIES_SIDEBAR = (By.XPATH, "//div[@class='left-sidebar']/h2")
    RECOMMENDED_ADD_TO_CART_BUTTONS = (By.XPATH, "//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart']")
    RECOMMENDED_ITEMS_HEADER = (By.XPATH, "//div[@class='recommended_items']//h2[normalize-space()='recommended items']")
    RECOMMENDED_PRODUCTS = (By.XPATH, "//div[@class='recommended_items']//div[@class='productinfo text-center']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/"
    
    def navigate_to_home(self) -> bool:
        """Navigate to the home page."""
        return self.navigate_to_url(self.page_url)
    
    def is_home_page_loaded(self) -> bool:
        """Check if home page is loaded successfully."""
        return self.is_logo_displayed()
    
    def scroll_to_subscription(self) -> bool:
        """Scroll to the subscription section."""
        return self.helper.scroll_to_element(self.SUBSCRIPTION_HEADER)
    
    def is_subscription_visible(self) -> bool:
        """Check if subscription section is visible."""
        return self.helper.is_element_displayed(self.SUBSCRIPTION_HEADER)
    
    def get_subscription_text(self) -> str:
        """Get the subscription header text."""
        return self.helper.get_element_text(self.SUBSCRIPTION_HEADER)
    
    def subscribe_to_newsletter(self, email: str) -> bool:
        """Subscribe to newsletter with given email."""
        try:
            # Enter email in subscription field
            if not self.helper.send_keys_to_element(self.SUBSCRIPTION_EMAIL, email):
                return False
            
            # Click subscribe button
            if not self.helper.click_element(self.SUBSCRIPTION_BUTTON):
                return False
            
            logger.info(f"Subscribed to newsletter with email: {email}")
            return True
        except Exception as e:
            logger.error(f"Failed to subscribe to newsletter: {e}")
            return False
    
    def is_subscription_successful(self) -> bool:
        """Check if subscription was successful."""
        return self.helper.is_element_displayed(self.SUBSCRIPTION_SUCCESS_MESSAGE)
    
    def get_subscription_success_message(self) -> str:
        """Get the subscription success message."""
        return self.helper.get_element_text(self.SUBSCRIPTION_SUCCESS_MESSAGE)
    
    def is_features_section_visible(self) -> bool:
        """Check if features section is visible."""
        return self.helper.is_element_displayed(self.FEATURES_ITEMS)
    
    def is_recommended_items_visible(self) -> bool:
        """Check if recommended items section is visible."""
        return self.helper.is_element_displayed(self.RECOMMENDED_ITEMS)
    
    def click_women_category(self) -> bool:
        """Click on Women category."""
        return self.helper.click_element(self.CATEGORY_WOMEN)
    
    def click_men_category(self) -> bool:
        """Click on Men category."""
        return self.helper.click_element(self.CATEGORY_MEN)
    
    def click_kids_category(self) -> bool:
        """Click on Kids category."""
        return self.helper.click_element(self.CATEGORY_KIDS)
    
    def click_test_cases(self) -> bool:
        """Click on Test Cases button."""
        return self.helper.click_element(self.TEST_CASES_BUTTON)
    
    def is_test_cases_page_loaded(self) -> bool:
        """Check if test cases page is loaded."""
        return self.helper.is_element_displayed(self.TEST_CASES_HEADER)
    
    def get_test_cases_header_text(self) -> str:
        """Get the test cases page header text."""
        return self.helper.get_element_text(self.TEST_CASES_HEADER)
    
    def verify_home_page_elements(self) -> dict:
        """Verify all home page elements and return status."""
        return {
            'logo_displayed': self.is_logo_displayed(),
            'features_visible': self.is_features_section_visible(),
            'recommended_items_visible': self.is_recommended_items_visible(),
            'subscription_visible': self.is_subscription_visible()
        }
    
    def is_categories_visible(self) -> bool:
        """Check if categories are visible on left sidebar."""
        return self.helper.is_element_displayed(self.CATEGORIES_SIDEBAR)
    
    def click_women_category(self) -> bool:
        """Click on Women category."""
        return self.helper.click_element(self.CATEGORY_WOMEN)
    
    def click_men_category(self) -> bool:
        """Click on Men category."""
        return self.helper.click_element(self.CATEGORY_MEN)
    
    def add_recommended_item_to_cart(self, index: int = 0) -> bool:
        """Add recommended item to cart."""
        try:
            # Find the recommended items add to cart buttons
            add_to_cart_buttons = self.driver.find_elements(*self.RECOMMENDED_ADD_TO_CART_BUTTONS)
            if index < len(add_to_cart_buttons):
                add_to_cart_buttons[index].click()
                logger.info(f"Added recommended item {index} to cart")
                return True
            else:
                logger.error(f"Recommended item {index} not found")
                return False
        except Exception as e:
            logger.error(f"Failed to add recommended item {index} to cart: {e}")
            return False
    
    def scroll_to_recommended_items(self) -> bool:
        """Scroll to recommended items section."""
        try:
            recommended_items = self.driver.find_element(*self.RECOMMENDED_ITEMS)
            self.driver.execute_script("arguments[0].scrollIntoView();", recommended_items)
            logger.info("Scrolled to recommended items section")
            return True
        except Exception as e:
            logger.error(f"Failed to scroll to recommended items: {e}")
            return False
    
    def verify_recommended_items_elements(self) -> dict:
        """Verify all recommended items elements and return status."""
        return {
            'recommended_items_visible': self.is_recommended_items_visible(),
            'recommended_items_header_visible': self.helper.is_element_displayed(self.RECOMMENDED_ITEMS_HEADER),
            'recommended_products_visible': self.helper.is_element_displayed(self.RECOMMENDED_PRODUCTS)
        }
    
    def verify_test_cases_page_elements(self) -> dict:
        """Verify all test cases page elements and return status."""
        return {
            'test_cases_header_visible': self.is_test_cases_page_loaded(),
            'test_cases_content_visible': self.helper.is_element_displayed(self.TEST_CASES_CONTENT)
        }
