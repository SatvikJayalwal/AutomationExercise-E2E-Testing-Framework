import pytest
import yaml
from utils.driver_factory import DriverFactory

# Load config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

# Load test data
with open("data/test_data.yaml") as f:
    test_data = yaml.safe_load(f)

# Fixture for initializing driver for Chrome and Edge
@pytest.fixture(params=config['browsers'])
def driver(request):
    # Initialize driver using DriverFactory
    driver = DriverFactory.get_driver(request.param)
    # Navigate to base URL
    driver.get(config['base_url'])
    yield driver
    # Quit driver after test
    DriverFactory.quit_driver()

# Fixture to provide user data to tests
@pytest.fixture
def user_data():
    return test_data['user']
    