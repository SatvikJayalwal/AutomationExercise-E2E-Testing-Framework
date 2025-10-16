"""
Utils package for the AutomationExercise testing framework.
"""
from .logger import logger
from .helpers import DataReader, WebDriverHelper, DataGenerator, ScreenshotHelper, APIHelper
from .reporting import allure_reporter, test_reporter, performance_reporter
from .screenshot_utils import ScreenshotManager, screenshot_on_failure

__all__ = [
    'logger',
    'DataReader', 
    'WebDriverHelper',
    'DataGenerator',
    'ScreenshotHelper',
    'APIHelper',
    'allure_reporter',
    'test_reporter',
    'performance_reporter',
    'ScreenshotManager',
    'screenshot_on_failure'
]