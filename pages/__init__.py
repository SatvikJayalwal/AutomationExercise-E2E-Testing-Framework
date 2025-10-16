"""
Pages package for the AutomationExercise testing framework.
"""
from .base_page import BasePage
from .home_page import HomePage
from .login_page import LoginPage
from .signup_page import SignupPage
from .account_info_page import AccountInfoPage
from .products_page import ProductsPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage
from .contact_page import ContactPage

__all__ = [
    'BasePage',
    'HomePage',
    'LoginPage', 
    'SignupPage',
    'AccountInfoPage',
    'ProductsPage',
    'CartPage',
    'CheckoutPage',
    'ContactPage'
]
