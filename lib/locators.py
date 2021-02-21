"""
locators.py: Implements class for page element locators

__author__ = "Don Ariston Urbano"
__credits__ = ["https://selenium-python.readthedocs.io/index.html"]
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPageLocators(object):
    """ Main page elements locator"""
    HOME_LINK = (By.ID, 'nav-home')
    CONTACT_LINK = (By.ID, 'nav-contact')
    SHOP_LINK = (By.ID, 'nav-shop')
    CART_LINK = (By.ID, 'nav-cart')
    TITLE = (By.CSS_SELECTOR, 'head>title')

    SUCCESS_MSG = {"message": (By.CSS_SELECTOR, '.alert'),
                   "back_button": (By.CSS_SELECTOR, 'a.btn:nth-child(2)')}

class ContactPageLocators(object):
    """ Contact page elements locator"""
    GO_BUTTON = (By.CSS_SELECTOR, '.btn-contact')
    FORM_FIELDS = {"forename": (By.CSS_SELECTOR, 'input#forename'),
                   "email": (By.CSS_SELECTOR, 'input#email'),
                   "msg": (By.CSS_SELECTOR, 'textarea#message')}

    FORM_WARNINGS = {"forename": (By.ID, 'forename-err'),
                     "email": (By.ID, 'email-err'),
                     "msg": (By.ID, 'message-err'),
                     "header": (By.ID, "header-message")}

class ShopPageLocators(object):
    """ Shop page elements locator"""
    PRODUCT_ITEMS = {"searchtype" : By.CSS_SELECTOR,
                     "name": '#product-{}>div>h4',
                     "price": '#product-{}>div>p>span',
                     "button": '#product-{}>div>p>a',
                     "list" : '.products>ul'}

class CartPageLocators(object):
    """ Cart page elements locator"""
    INFO = {"warning" : (By.CSS_SELECTOR, '.alert'),
            "header" : (By.CSS_SELECTOR, '.cart-msg'),
            "totalcount" : (By.CSS_SELECTOR, '.cart-count')}
    CART_ITEMS = {"searchtype": By.XPATH,
                  "qty": '/html/body/div[2]/div/form/table/tbody/tr[{}]/td[3]/input',
                  "name": '/html/body/div[2]/div/form/table/tbody/tr[{}]/td[1]'}
