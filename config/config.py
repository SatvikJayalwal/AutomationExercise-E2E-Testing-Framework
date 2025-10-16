"""
Configuration settings for the AutomationExercise testing framework.
"""
import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Base URLs
BASE_URL = "https://www.automationexercise.com"
API_BASE_URL = "https://automationexercise.com/api"

# Browser configurations
BROWSER_CONFIG = {
    "chrome": {
        "driver_path": None,  # Will use system PATH
        "options": [
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--window-size=1920,1080"
        ]
    },
    "edge": {
        "driver_path": None,
        "options": []
    }
}

# Test data paths
DATA_DIR = PROJECT_ROOT / "data"
TEST_DATA_FILE = DATA_DIR / "test_data.json"
USER_DATA_FILE = DATA_DIR / "user_data.csv"

# Logging configuration
LOG_DIR = PROJECT_ROOT / "logs"
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Screenshot configuration
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"

# Reports configuration
REPORTS_DIR = PROJECT_ROOT / "reports"
ALLURE_RESULTS_DIR = REPORTS_DIR / "allure-results"

# Wait configurations
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
POLL_FREQUENCY = 0.5

# Test execution configuration
PARALLEL_WORKERS = 4
RETRY_COUNT = 2

# Environment variables
ENVIRONMENT = os.getenv("TEST_ENV", "staging")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# API configuration
API_TIMEOUT = 30
API_RETRY_COUNT = 3

# Database configuration (if needed)
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "automation_exercise"),
    "username": os.getenv("DB_USER", ""),
    "password": os.getenv("DB_PASSWORD", "")
}
