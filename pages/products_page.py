"""
Products page class for the AutomationExercise testing framework.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger


class ProductsPage(BasePage):
    """Products page class containing locators and methods for the products page."""
    
    # Products page locators
    PRODUCTS_HEADER = (By.XPATH, "//h2[@class='title text-center']")
    SEARCH_PRODUCT_INPUT = (By.XPATH, "//input[@id='search_product']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='submit_search']")
    SEARCHED_PRODUCTS = (By.XPATH, "//div[@class='productinfo text-center']")
    PRODUCT_NAMES = (By.XPATH, "//div[@class='productinfo text-center']//p")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//a[@data-product-id]")
    VIEW_PRODUCT_BUTTONS = (By.XPATH, "//a[contains(@href, '/product_details/')]")
    BRAND_FILTER = (By.XPATH, "//div[@class='brands_products']")
    CATEGORY_FILTER = (By.XPATH, "//div[@class='category-products']")
    PRODUCT_DETAIL_IMAGE = (By.XPATH, "//img[@alt='ecommerce website products']")
    PRODUCT_INFORMATION = (By.XPATH, "//div[@class='product-information']")
    CATEGORY_WOMEN = (By.XPATH, "//a[@href='#Women']")
    CATEGORY_MEN = (By.XPATH, "//a[@href='#Men']")
    CATEGORY_KIDS = (By.XPATH, "//a[@href='#Kids']")
    PRODUCT_DETAIL_NAME = (By.XPATH, "//div[@class='product-information']/h2")
    PRODUCT_QUANTITY_INPUT = (By.XPATH, "//input[@id='quantity']")
    ADD_TO_CART_DETAIL_BUTTON = (By.XPATH, "//button[@class='btn btn-default cart']")
    WOMEN_TOPS_CATEGORY = (By.XPATH, "//a[@href='/category_products/2']")
    MEN_JEANS_CATEGORY = (By.XPATH, "//a[@href='/category_products/6']")
    WOMEN_TOPS_PRODUCTS = (By.XPATH, "//div[@class='features_items']//h2[contains(normalize-space(),'Women - Tops Products')]")
    MEN_JEANS_PRODUCTS = (By.XPATH, "//div[@class='features_items']//h2[contains(normalize-space(),'Men - Jeans Products')]")
    CATEGORY_PRODUCTS = (By.XPATH, "//div[@class='features_items']")
    BRAND_HM = (By.XPATH, "//a[@href='/brand_products/H&M']")
    BRAND_POLO = (By.XPATH, "//a[@href='/brand_products/Polo']")
    BRAND_HM_PRODUCTS = (By.XPATH, "//div[@class='features_items']//h2[contains(normalize-space(),'Brand - H&M Products')]")
    BRAND_POLO_PRODUCTS = (By.XPATH, "//div[@class='features_items']//h2[contains(normalize-space(),'Brand - Polo Products')]")
    BRAND_PRODUCTS = (By.XPATH, "//div[@class='features_items']")
    WRITE_REVIEW_SECTION = (By.XPATH, "//a[@href='#reviews']")
    REVIEW_NAME_INPUT = (By.XPATH, "//input[@id='name']")
    REVIEW_EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    REVIEW_TEXT_INPUT = (By.XPATH, "//textarea[@id='review']")
    REVIEW_SUBMIT_BUTTON = (By.XPATH, "//button[@id='button-review']")
    REVIEW_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert-success alert' and contains(normalize-space(), 'Thank you for your review.')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.automationexercise.com/products"
    
    def navigate_to_products(self) -> bool:
        """Navigate to the products page."""
        return self.navigate_to_url(self.page_url)
    
    def is_products_page_loaded(self) -> bool:
        """Check if products page is loaded."""
        return self.helper.is_element_displayed(self.PRODUCTS_HEADER)
    
    def get_products_header_text(self) -> str:
        """Get the products page header text."""
        return self.helper.get_element_text(self.PRODUCTS_HEADER)
    
    def search_product(self, search_term: str) -> bool:
        """Search for a product."""
        try:
            # Enter search term
            if not self.helper.send_keys_to_element(self.SEARCH_PRODUCT_INPUT, search_term):
                return False
            
            # Click search button
            if not self.helper.click_element(self.SEARCH_BUTTON):
                return False
            
            logger.info(f"Searched for product: {search_term}")
            return True
        except Exception as e:
            logger.error(f"Failed to search product: {e}")
            return False
    
    def are_searched_products_visible(self) -> bool:
        """Check if searched products are visible."""
        return self.helper.is_element_displayed(self.SEARCHED_PRODUCTS)
    
    def get_product_names(self) -> list:
        """Get list of product names."""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_NAMES)
            return [element.text for element in elements]
        except Exception as e:
            logger.error(f"Failed to get product names: {e}")
            return []
    
    def add_product_to_cart(self, product_index: int = 0) -> bool:
        """Add a product to cart by index."""
        try:
            add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
            if product_index < len(add_to_cart_buttons):
                add_to_cart_buttons[product_index].click()
                logger.info(f"Added product {product_index} to cart")
                return True
            else:
                logger.error(f"Product index {product_index} out of range")
                return False
        except Exception as e:
            logger.error(f"Failed to add product to cart: {e}")
            return False
    
    def view_product_details(self, product_index: int = 0) -> bool:
        """View product details by index."""
        try:
            view_product_buttons = self.driver.find_elements(*self.VIEW_PRODUCT_BUTTONS)
            if product_index < len(view_product_buttons):
                view_product_buttons[product_index].click()
                logger.info(f"Viewed product {product_index} details")
                return True
            else:
                logger.error(f"Product index {product_index} out of range")
                return False
        except Exception as e:
            logger.error(f"Failed to view product details: {e}")
            return False
    
    def is_brand_filter_visible(self) -> bool:
        """Check if brand filter is visible."""
        return self.helper.is_element_displayed(self.BRAND_FILTER)
    
    def is_category_filter_visible(self) -> bool:
        """Check if category filter is visible."""
        return self.helper.is_element_displayed(self.CATEGORY_FILTER)
    
    def is_product_detail_page_loaded(self) -> bool:
        """Check if product detail page is loaded."""
        return self.helper.is_element_displayed(self.PRODUCT_DETAIL_IMAGE)
    
    def is_product_information_visible(self) -> bool:
        """Check if product information is visible."""
        return self.helper.is_element_displayed(self.PRODUCT_INFORMATION)
    
    def click_women_category(self) -> bool:
        """Click on Women category."""
        return self.helper.click_element(self.CATEGORY_WOMEN)
    
    def click_men_category(self) -> bool:
        """Click on Men category."""
        return self.helper.click_element(self.CATEGORY_MEN)
    
    def click_kids_category(self) -> bool:
        """Click on Kids category."""
        return self.helper.click_element(self.CATEGORY_KIDS)
    
    def get_product_name_from_detail_page(self) -> str:
        """Get product name from detail page."""
        try:
            element = self.driver.find_element(*self.PRODUCT_DETAIL_NAME)
            return element.text
        except Exception as e:
            logger.error(f"Failed to get product name from detail page: {e}")
            return ""
    
    def set_product_quantity(self, quantity: int) -> bool:
        """Set product quantity on detail page."""
        try:
            quantity_input = self.driver.find_element(*self.PRODUCT_QUANTITY_INPUT)
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))
            logger.info(f"Set product quantity to {quantity}")
            return True
        except Exception as e:
            logger.error(f"Failed to set product quantity: {e}")
            return False
    
    def add_to_cart_from_detail_page(self) -> bool:
        """Add product to cart from detail page."""
        try:
            add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_DETAIL_BUTTON)
            add_to_cart_button.click()
            logger.info("Added product to cart from detail page")
            return True
        except Exception as e:
            logger.error(f"Failed to add product to cart from detail page: {e}")
            return False
    
    def click_women_tops(self) -> bool:
        """Click on Women Tops category."""
        return self.helper.click_element(self.WOMEN_TOPS_CATEGORY)
    
    def click_men_jeans(self) -> bool:
        """Click on Men Jeans category."""
        return self.helper.click_element(self.MEN_JEANS_CATEGORY)
    
    def is_women_tops_products_visible(self) -> bool:
        """Check if Women Tops products are visible."""
        return self.helper.is_element_displayed(self.WOMEN_TOPS_PRODUCTS)
    
    def is_men_jeans_products_visible(self) -> bool:
        """Check if Men Jeans products are visible."""
        return self.helper.is_element_displayed(self.MEN_JEANS_PRODUCTS)
    
    def get_women_tops_products_text(self) -> str:
        """Get Women Tops products text."""
        return self.helper.get_element_text(self.WOMEN_TOPS_PRODUCTS)
    
    def get_men_jeans_products_text(self) -> str:
        """Get Men Jeans products text."""
        return self.helper.get_element_text(self.MEN_JEANS_PRODUCTS)
    
    def are_category_products_visible(self) -> bool:
        """Check if category products are visible."""
        return self.helper.is_element_displayed(self.CATEGORY_PRODUCTS)
    
    def click_brand_hm(self) -> bool:
        """Click on H&M brand."""
        return self.helper.click_element(self.BRAND_HM)
    
    def click_brand_polo(self) -> bool:
        """Click on Polo brand."""
        return self.helper.click_element(self.BRAND_POLO)
    
    def is_brand_hm_products_visible(self) -> bool:
        """Check if H&M brand products are visible."""
        return self.helper.is_element_displayed(self.BRAND_HM_PRODUCTS)
    
    def is_brand_polo_products_visible(self) -> bool:
        """Check if Polo brand products are visible."""
        return self.helper.is_element_displayed(self.BRAND_POLO_PRODUCTS)
    
    def get_brand_hm_products_text(self) -> str:
        """Get H&M brand products text."""
        return self.helper.get_element_text(self.BRAND_HM_PRODUCTS)
    
    def get_brand_polo_products_text(self) -> str:
        """Get Polo brand products text."""
        return self.helper.get_element_text(self.BRAND_POLO_PRODUCTS)
    
    def are_brand_products_visible(self) -> bool:
        """Check if brand products are visible."""
        return self.helper.is_element_displayed(self.BRAND_PRODUCTS)
    
    def is_write_review_visible(self) -> bool:
        """Check if Write Your Review section is visible."""
        return self.helper.is_element_displayed(self.WRITE_REVIEW_SECTION)
    
    def enter_review_name(self, name: str) -> bool:
        """Enter review name."""
        return self.helper.send_keys_to_element(self.REVIEW_NAME_INPUT, name)
    
    def enter_review_email(self, email: str) -> bool:
        """Enter review email."""
        return self.helper.send_keys_to_element(self.REVIEW_EMAIL_INPUT, email)
    
    def enter_review_text(self, review: str) -> bool:
        """Enter review text."""
        return self.helper.send_keys_to_element(self.REVIEW_TEXT_INPUT, review)
    
    def submit_review(self) -> bool:
        """Submit review."""
        return self.helper.click_element(self.REVIEW_SUBMIT_BUTTON)
    
    def is_review_success_message_visible(self) -> bool:
        """Check if review success message is visible."""
        return self.helper.is_element_displayed(self.REVIEW_SUCCESS_MESSAGE)
    
    def get_review_success_message(self) -> str:
        """Get review success message."""
        return self.helper.get_element_text(self.REVIEW_SUCCESS_MESSAGE)
    
    def clear_review_form(self) -> bool:
        """Clear review form."""
        try:
            self.helper.clear_element(self.REVIEW_NAME_INPUT)
            self.helper.clear_element(self.REVIEW_EMAIL_INPUT)
            self.helper.clear_element(self.REVIEW_TEXT_INPUT)
            return True
        except Exception as e:
            logger.error(f"Failed to clear review form: {e}")
            return False
    
    def verify_review_form_elements(self) -> dict:
        """Verify all review form elements and return status."""
        return {
            'write_review_visible': self.is_write_review_visible(),
            'review_name_field_visible': self.helper.is_element_displayed(self.REVIEW_NAME_INPUT),
            'review_email_field_visible': self.helper.is_element_displayed(self.REVIEW_EMAIL_INPUT),
            'review_text_field_visible': self.helper.is_element_displayed(self.REVIEW_TEXT_INPUT),
            'submit_button_visible': self.helper.is_element_displayed(self.REVIEW_SUBMIT_BUTTON)
        }
    
    def verify_products_page_elements(self) -> dict:
        """Verify all products page elements and return status."""
        return {
            'products_header_visible': self.is_products_page_loaded(),
            'brand_filter_visible': self.is_brand_filter_visible(),
            'category_filter_visible': self.is_category_filter_visible()
        }
