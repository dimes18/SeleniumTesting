"""
page.py: Implements reusable code for handling/interfacing different
         pages for automation

__author__ = "Don Ariston Urbano"
__credits__ = ["https://selenium-python.readthedocs.io/index.html"]
"""

import time
from lib.element import BasePageElement
from lib.locators import MainPageLocators, \
                         ContactPageLocators, \
                         ShopPageLocators, \
                         CartPageLocators, \
                         Keys

class SearchElement(BasePageElement):
    """ Inherit Descriptor class  """
    pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def slow_typing(element, input_value, delay):
        """ Simulate keyboard typing """
        for char in input_value:
            element.send_keys(char)
            time.sleep(delay)

    wait_for_back_button = SearchElement(resource=MainPageLocators.SUCCESS_MSG['back_button'])
    wait_for_warning_header = SearchElement(resource=ContactPageLocators.FORM_WARNINGS['header'])
    wait_for_forename_err = SearchElement(resource=ContactPageLocators.FORM_WARNINGS['forename'])
    wait_for_email_err = SearchElement(resource=ContactPageLocators.FORM_WARNINGS['email'])
    wait_for_msg_err = SearchElement(resource=ContactPageLocators.FORM_WARNINGS['msg'])

class MainPage(BasePage):
    """Home Page methods"""

    def is_title_matches(self, keyword):
        """Verifies if keyword appears in page title"""
        return keyword in self.driver.title

    def go_home_page(self):
        """Click home """
        try:
            element = self.driver.find_element(*MainPageLocators.HOME_LINK)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def go_contact_page(self):
        """Click shop contact item"""
        try:
            element = self.driver.find_element(*MainPageLocators.CONTACT_LINK)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def go_shop_page(self):
        """Click shop menu item"""
        try:
            element = self.driver.find_element(*MainPageLocators.SHOP_LINK)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def go_cart_page(self):
        """Click cart menu item"""
        try:
            element = self.driver.find_element(*MainPageLocators.CART_LINK)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

class ContactPage(BasePage):
    """Contact Page methods"""

    def click_go_button(self):
        """Triggers the submit"""
        try:
            element = self.driver.find_element(*ContactPageLocators.GO_BUTTON)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def populate_required_fields(self, **kwargs):
        """fill up the form"""
        assert kwargs is not None, "Missing kwargs!"
        try:
            for key in kwargs:
                assert key in ContactPageLocators.FORM_FIELDS
                element = self.driver.find_element(*ContactPageLocators.FORM_FIELDS[key])
                self.slow_typing(element, kwargs[key], 0.3)
                self.slow_typing(element, Keys.TAB, 0.3)
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def validate_form_errors(self, *args):
        """check if no form errors"""
        assert args is not None, "Missing args!"
        result = True
        time.sleep(0.1)
        try:
            for key in args:
                assert key in ContactPageLocators.FORM_WARNINGS
                try:
                    element = self.driver.find_element(*ContactPageLocators.FORM_WARNINGS[key])
                    if element.text:
                        result = False
                except Exception as err:
                    continue
            return result
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def validate_submission_message(self):
        """Check submission result message"""
        try:
            element = self.driver.find_element(*MainPageLocators.SUCCESS_MSG['message'])
            return element.text
        except Exception as err:
            print("Error: {}".format(err))
        return None

class ShopPage(BasePage):
    """Shop Page methods"""

    def _total_products(self):
        """Count total number of shop items"""
        element = self.driver.find_element(ShopPageLocators.PRODUCT_ITEMS["searchtype"],
                                           ShopPageLocators.PRODUCT_ITEMS["list"])
        total = element.get_attribute("childElementCount")
        return total

    def find_item_locators(self, buyitems=dict):
        """find the locator of the selected products"""
        assert buyitems is not None, "Missing items to buy!"
        locators = {}
        try:
            total = int(self._total_products())
            for idx in range(total):
                product_name = ShopPageLocators.PRODUCT_ITEMS["name"]
                product_button = ShopPageLocators.PRODUCT_ITEMS["button"]
                element = self.driver.find_element(ShopPageLocators.PRODUCT_ITEMS["searchtype"],
                                                   product_name.format(idx+1))
                product = element.get_attribute("innerText")
                for key in buyitems:
                    if key.lower() != product.lower():
                        continue
                    locators[key] = product_button.format(idx+1)
                    break
        except Exception as err:
            print("Error: {}".format(err))
        return locators

    def click_buy_product(self, locators, buyitems=dict):
        """Buy the selected product items"""
        assert len(locators) == len(buyitems), "Quantities not tally with Buy Items!"
        try:
            for product in locators:
                for key in buyitems:
                    if product != key:
                        continue
                    qty = buyitems[key]
                    for _ in range(qty):
                        element = self.driver.find_element(ShopPageLocators.PRODUCT_ITEMS["searchtype"],
                                                           locators[product])
                        element.click()
                        time.sleep(0.5)
            return True
        except Exception as err:
            print("Error: {}". format(err))
        return False

class CartPage(BasePage):
    """Shop Page methods"""

    def find_cart_item_locators(self, buyitems=dict):
        """find the locator of the cart items"""
        assert buyitems is not None, "Missing items to buy!"
        locators = {}
        try:
            total = len(buyitems)
            for idx in range(total):
                item_name = CartPageLocators.CART_ITEMS["name"]
                item_qty = CartPageLocators.CART_ITEMS["qty"]
                element = self.driver.find_element(CartPageLocators.CART_ITEMS["searchtype"],
                                                   item_name.format(idx+1))
                item = element.get_attribute("innerText")
                for key in buyitems:
                    if key.lower() in item.lower():
                        locators[key] = item_qty.format(idx+1)
                        break

        except Exception as err:
            print("Cart Items Error: {}".format(err))
        return locators

    def click_empty_cart(self):
        """TODO"""
        pass

    def get_total_quantity(self):
        """TODO"""
        pass

    def compare_product_quantity(self, locators, buyitems=dict):
        """Verify if items selected is in correct quantity"""
        assert len(locators) == len(buyitems), "Buy items not tally with Cart Items!"
        result = True
        try:
            for cart_item in locators:
                for key in buyitems:
                    if cart_item != key:
                        continue
                    qty = buyitems[key]
                    element = self.driver.find_element(CartPageLocators.CART_ITEMS["searchtype"],
                                                       locators[cart_item])
                    cart_item_qty = element.get_attribute("value")
                    if qty != int(cart_item_qty):
                        result = False
                    break
            return result
        except Exception as err:
            print("Cart Quantity Error: {}". format(err))
        return False
