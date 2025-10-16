"""
Logging utility for the AutomationExercise testing framework.
"""
import logging
import os
from datetime import datetime
from pathlib import Path
from config.config import LOG_DIR, LOG_LEVEL, LOG_FORMAT


class Logger:
    """Custom logger class for the testing framework."""
    
    _instance = None
    _logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._logger is None:
            self._setup_logger()
    
    def _setup_logger(self):
        """Setup the logger configuration."""
        # Create logs directory if it doesn't exist
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        
        # Create logger
        self._logger = logging.getLogger("AutomationExercise")
        self._logger.setLevel(getattr(logging, LOG_LEVEL.upper()))
        
        # Clear existing handlers
        self._logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter(LOG_FORMAT)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)
        
        # File handler
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = LOG_DIR / f"automation_exercise_{timestamp}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)
    
    def get_logger(self):
        """Get the logger instance."""
        return self._logger
    
    def info(self, message):
        """Log info message."""
        self._logger.info(message)
    
    def debug(self, message):
        """Log debug message."""
        self._logger.debug(message)
    
    def warning(self, message):
        """Log warning message."""
        self._logger.warning(message)
    
    def error(self, message):
        """Log error message."""
        self._logger.error(message)
    
    def critical(self, message):
        """Log critical message."""
        self._logger.critical(message)


# Global logger instance
logger = Logger().get_logger()
