import pytest
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage
from pages.account_page import AccountPage

# Test case: Register a new user, verify login, and delete the account
def test_register_user(driver, user_data):
    # Initialize HomePage object with the driver
    home_page = HomePage(driver)
    
    # Verify the home page logo is visible to ensure the page loaded successfully
    home_page.verify_home_page()
    
    # Click on the 'Signup / Login' button to navigate to the signup page
    home_page.go_to_signup_login()

    # Initialize SignupLoginPage object
    signup_page = SignupLoginPage(driver)
    
    # Verify the 'New User Signup!' form is visible
    signup_page.verify_signup_form()
    
    # Enter the user's name and email into the signup form
    signup_page.enter_signup_details(user_data['name'], user_data['email'])
    
    # Click the 'Signup' button to proceed to account creation
    signup_page.click_signup()

    # Initialize AccountCreationPage object
    account_creation_page = AccountCreationPage(driver)
    
    # Fill in all required account creation details using the user_data fixture
    account_creation_page.fill_account_info(user_data)
    
    # Click 'Create Account' to submit the form
    account_creation_page.create_account()

    # Initialize AccountPage object to verify account creation
    account_page = AccountPage(driver)
    
    # Verify that 'ACCOUNT CREATED!' message is visible on the page
    account_page.verify_account_created()
    
    # Click the 'Continue' button after account creation
    account_page.continue_after_creation()
    
    # Verify that the user is logged in by checking the username displayed
    account_page.verify_logged_in_user(user_data['name'])
    
    # Click the 'Delete Account' button to remove the account
    account_page.delete_account()
    
    # Verify that 'ACCOUNT DELETED!' message is displayed confirming deletion
    account_page.verify_account_deleted()
    
    # Click the 'Continue' button after account deletion
    account_page.continue_after_deletion()
