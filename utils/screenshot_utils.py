"""
Screenshot utilities for the AutomationExercise testing framework.
"""
import os
import allure
from datetime import datetime
from pathlib import Path
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from config.config import SCREENSHOT_DIR
from utils.logger import logger


class ScreenshotManager:
    """Enhanced screenshot management for test failures and debugging."""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.screenshot_dir = SCREENSHOT_DIR
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
    
    def take_screenshot(self, filename: str = None, attach_to_allure: bool = True) -> str:
        """Take a screenshot and optionally attach to Allure report."""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
                filename = f"screenshot_{timestamp}.png"
            
            # Ensure filename has .png extension
            if not filename.endswith('.png'):
                filename += '.png'
            
            file_path = self.screenshot_dir / filename
            
            # Take screenshot
            self.driver.save_screenshot(str(file_path))
            logger.info(f"Screenshot saved: {file_path}")
            
            # Attach to Allure if requested
            if attach_to_allure:
                self.attach_to_allure(str(file_path), filename)
            
            return str(file_path)
            
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return ""
    
    def take_screenshot_on_failure(self, test_name: str, error_message: str = None) -> str:
        """Take a screenshot when a test fails."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        error_suffix = f"_{error_message[:20].replace(' ', '_')}" if error_message else ""
        filename = f"{test_name}_failure{error_suffix}_{timestamp}.png"
        return self.take_screenshot(filename, attach_to_allure=True)
    
    def take_screenshot_on_error(self, error_message: str, test_name: str = None) -> str:
        """Take a screenshot when an error occurs."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        test_suffix = f"_{test_name}" if test_name else ""
        error_suffix = error_message[:20].replace(' ', '_') if error_message else "error"
        filename = f"error{test_suffix}_{error_suffix}_{timestamp}.png"
        return self.take_screenshot(filename, attach_to_allure=True)
    
    def take_screenshot_on_assertion_failure(self, assertion_message: str, test_name: str = None) -> str:
        """Take a screenshot when an assertion fails."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        test_suffix = f"_{test_name}" if test_name else ""
        assertion_suffix = assertion_message[:20].replace(' ', '_') if assertion_message else "assertion"
        filename = f"assertion_failure{test_suffix}_{assertion_suffix}_{timestamp}.png"
        return self.take_screenshot(filename, attach_to_allure=True)
    
    def take_screenshot_before_action(self, action_name: str, test_name: str = None) -> str:
        """Take a screenshot before performing an action."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        test_suffix = f"_{test_name}" if test_name else ""
        action_suffix = action_name[:20].replace(' ', '_') if action_name else "action"
        filename = f"before_{action_suffix}{test_suffix}_{timestamp}.png"
        return self.take_screenshot(filename, attach_to_allure=False)
    
    def take_screenshot_after_action(self, action_name: str, test_name: str = None) -> str:
        """Take a screenshot after performing an action."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        test_suffix = f"_{test_name}" if test_name else ""
        action_suffix = action_name[:20].replace(' ', '_') if action_name else "action"
        filename = f"after_{action_suffix}{test_suffix}_{timestamp}.png"
        return self.take_screenshot(filename, attach_to_allure=False)
    
    def attach_to_allure(self, file_path: str, name: str = "Screenshot"):
        """Attach screenshot to Allure report."""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)
                logger.info(f"Screenshot attached to Allure report: {name}")
            else:
                logger.warning(f"Screenshot file not found for Allure attachment: {file_path}")
        except Exception as e:
            logger.error(f"Failed to attach screenshot to Allure report: {e}")
    
    def take_element_screenshot(self, element, filename: str = None) -> str:
        """Take a screenshot of a specific element."""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
                filename = f"element_screenshot_{timestamp}.png"
            
            if not filename.endswith('.png'):
                filename += '.png'
            
            file_path = self.screenshot_dir / filename
            
            # Take element screenshot
            element.screenshot(str(file_path))
            logger.info(f"Element screenshot saved: {file_path}")
            
            # Attach to Allure
            self.attach_to_allure(str(file_path), f"Element Screenshot: {filename}")
            
            return str(file_path)
            
        except Exception as e:
            logger.error(f"Failed to take element screenshot: {e}")
            return ""
    
    def take_full_page_screenshot(self, filename: str = None) -> str:
        """Take a full page screenshot (including scrolled content)."""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
                filename = f"full_page_screenshot_{timestamp}.png"
            
            if not filename.endswith('.png'):
                filename += '.png'
            
            file_path = self.screenshot_dir / filename
            
            # Get full page dimensions
            total_width = self.driver.execute_script("return document.body.scrollWidth")
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # Set window size to full page
            self.driver.set_window_size(total_width, total_height)
            
            # Take screenshot
            self.driver.save_screenshot(str(file_path))
            logger.info(f"Full page screenshot saved: {file_path}")
            
            # Attach to Allure
            self.attach_to_allure(str(file_path), f"Full Page Screenshot: {filename}")
            
            return str(file_path)
            
        except Exception as e:
            logger.error(f"Failed to take full page screenshot: {e}")
            return ""


def screenshot_on_failure(test_name: str, error_message: str = None):
    """Decorator to automatically take screenshots on test failure."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Try to get driver from args or kwargs
                driver = None
                for arg in args:
                    if hasattr(arg, 'save_screenshot'):
                        driver = arg
                        break
                
                if not driver:
                    for key, value in kwargs.items():
                        if hasattr(value, 'save_screenshot'):
                            driver = value
                            break
                
                if driver:
                    screenshot_manager = ScreenshotManager(driver)
                    screenshot_manager.take_screenshot_on_failure(test_name, str(e))
                
                raise e
        return wrapper
    return decorator
