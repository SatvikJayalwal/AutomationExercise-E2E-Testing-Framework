"""
Helper utilities for the AutomationExercise testing framework.
"""
import json
import csv
import yaml
import time
import random
import string
from pathlib import Path
from typing import Dict, List, Any, Union
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import DATA_DIR, IMPLICIT_WAIT, EXPLICIT_WAIT, POLL_FREQUENCY
from utils.logger import logger


class DataReader:
    """Utility class for reading test data from various file formats."""
    
    @staticmethod
    def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:
        """Read data from JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logger.error(f"JSON file not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format in {file_path}: {e}")
            return {}
    
    @staticmethod
    def read_csv(file_path: Union[str, Path]) -> List[Dict[str, str]]:
        """Read data from CSV file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            logger.error(f"CSV file not found: {file_path}")
            return []
    
    @staticmethod
    def read_yaml(file_path: Union[str, Path]) -> Dict[str, Any]:
        """Read data from YAML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logger.error(f"YAML file not found: {file_path}")
            return {}
        except yaml.YAMLError as e:
            logger.error(f"Invalid YAML format in {file_path}: {e}")
            return {}


class WebDriverHelper:
    """Helper class for common WebDriver operations."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT, poll_frequency=POLL_FREQUENCY)
        self.actions = ActionChains(driver)
    
    def wait_for_element(self, locator: tuple, timeout: int = None) -> bool:
        """Wait for element to be visible."""
        try:
            wait_time = timeout or EXPLICIT_WAIT
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            return False
    
    def wait_for_clickable(self, locator: tuple, timeout: int = None) -> bool:
        """Wait for element to be clickable."""
        try:
            wait_time = timeout or EXPLICIT_WAIT
            WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            return False
    
    def click_element(self, locator: tuple) -> bool:
        """Click on element with wait."""
        try:
            if self.wait_for_clickable(locator):
                element = self.driver.find_element(*locator)
                element.click()
                logger.info(f"Clicked element: {locator}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {e}")
            return False
    
    def send_keys_to_element(self, locator: tuple, text: str) -> bool:
        """Send keys to element with wait."""
        try:
            if self.wait_for_element(locator):
                element = self.driver.find_element(*locator)
                element.clear()
                element.send_keys(text)
                logger.info(f"Sent keys to element: {locator}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to send keys to element {locator}: {e}")
            return False
    
    def get_element_text(self, locator: tuple) -> str:
        """Get text from element."""
        try:
            if self.wait_for_element(locator):
                element = self.driver.find_element(*locator)
                return element.text
            return ""
        except Exception as e:
            logger.error(f"Failed to get text from element {locator}: {e}")
            return ""
    
    def is_element_displayed(self, locator: tuple) -> bool:
        """Check if element is displayed."""
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False
    
    def scroll_to_element(self, locator: tuple) -> bool:
        """Scroll to element."""
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info(f"Scrolled to element: {locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to scroll to element {locator}: {e}")
            return False
    
    def select_dropdown_by_text(self, locator: tuple, text: str) -> bool:
        """Select dropdown option by visible text."""
        try:
            if self.wait_for_element(locator):
                select = Select(self.driver.find_element(*locator))
                select.select_by_visible_text(text)
                logger.info(f"Selected '{text}' from dropdown: {locator}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to select dropdown option {locator}: {e}")
            return False
    
    def hover_element(self, locator: tuple) -> bool:
        """Hover over element."""
        try:
            if self.wait_for_element(locator):
                element = self.driver.find_element(*locator)
                self.actions.move_to_element(element).perform()
                logger.info(f"Hovered over element: {locator}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to hover over element {locator}: {e}")
            return False


class DataGenerator:
    """Utility class for generating test data."""
    
    @staticmethod
    def generate_random_email() -> str:
        """Generate random email address."""
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])
        return f"{username}@{domain}"
    
    @staticmethod
    def generate_random_name() -> str:
        """Generate random name."""
        first_names = ['John', 'Jane', 'Mike', 'Sarah', 'David', 'Lisa', 'Tom', 'Emma']
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    @staticmethod
    def generate_random_phone() -> str:
        """Generate random phone number."""
        return ''.join(random.choices(string.digits, k=10))
    
    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        """Generate random string."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class ScreenshotHelper:
    """Helper class for taking screenshots."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def take_screenshot(self, filename: str = None) -> str:
        """Take screenshot and return file path."""
        from config.config import SCREENSHOT_DIR
        from datetime import datetime
        
        # Create screenshots directory if it doesn't exist
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        
        # Generate filename if not provided
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
            filename = f"screenshot_{timestamp}.png"
        
        # Ensure filename has .png extension
        if not filename.endswith('.png'):
            filename += '.png'
        
        file_path = SCREENSHOT_DIR / filename
        
        try:
            self.driver.save_screenshot(str(file_path))
            logger.info(f"Screenshot saved: {file_path}")
            return str(file_path)
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return ""


class APIHelper:
    """Helper class for API operations."""
    
    @staticmethod
    def make_request(method: str, url: str, **kwargs) -> dict:
        """Make HTTP request and return response data."""
        import requests
        from config.config import API_TIMEOUT
        
        try:
            response = requests.request(method, url, timeout=API_TIMEOUT, **kwargs)
            logger.info(f"API {method} request to {url} - Status: {response.status_code}")
            
            # Try to parse JSON regardless of content-type
            try:
                json_data = response.json()
            except:
                json_data = None
            
            return {
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'text': response.text,
                'json': json_data
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return {'error': str(e)}
