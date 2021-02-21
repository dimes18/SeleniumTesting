"""
test_pages.py: Implements unittest for the lib.page.py functions

__author__ = "Don Ariston Urbano"
__version__ = "1.0.1"
"""
import unittest
import time
from selenium import webdriver
from lib import page

class PlanitTesting(unittest.TestCase):
    """Class for testing Planit test webpage"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_page = None
        self.contact_page = None
        self.shop_page = None
        self.cart_page = None

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://jupiter.cloud.planittesting.com")
        self.main_page = page.MainPage(self.driver)
        print("----------------------------------------------------------------------")
        print("===Executing Tests===")

    def _wait_for_back_button(self):
        value = self.contact_page.wait_for_back_button
        return 'back' in value.lower()

    def _wait_for_warning_header(self, keyword):
        value = self.contact_page.wait_for_warning_header
        return keyword in value.lower()

    def test_case_1(self):
        """
        Test for submit form errors in contact page
        """
        print("Step: {} - {}".format(self._testMethodName, self._testMethodDoc))
        self.assertTrue(self.main_page.go_home_page())
        self.assertTrue(self.main_page.go_contact_page())
        self.contact_page = page.ContactPage(self.driver)
        time.sleep(0.3)
        self.assertTrue(self.contact_page.click_go_button())
        self.assertFalse(self.contact_page.validate_form_errors("forename", "email", "msg"))
        self.assertTrue(self.contact_page.populate_required_fields(forename="Johnny",
                                                                   email="Johnny@jmail.com",
                                                                   msg="Thank you!"))
        self.assertTrue(self.contact_page.validate_form_errors("forename", "email", "msg"))
        self.assertTrue(self._wait_for_warning_header("tell it how it is"))

    def test_case_2(self):
        """
        Test for submit form submission is successful
        """
        print("Step: {} - {}".format(self._testMethodName, self._testMethodDoc))
        self.assertTrue(self.main_page.go_home_page())
        self.assertTrue(self.main_page.go_contact_page())
        self.contact_page = page.ContactPage(self.driver)
        time.sleep(0.3)
        self.assertTrue(self.contact_page.populate_required_fields(forename="Jonny",
                                                                   email="Jonny@jmail.com",
                                                                   msg="Cheers!"))
        self.assertTrue(self.contact_page.click_go_button())
        self.assertTrue(self._wait_for_back_button())
        self.assertIn("Thanks", self.contact_page.validate_submission_message())

    def test_case_3(self):
        """
        Test for submit form with invalid inputs
        """
        print("Step: {} - {}".format(self._testMethodName, self._testMethodDoc))
        self.assertTrue(self.main_page.go_home_page())
        self.assertTrue(self.main_page.go_contact_page())
        self.contact_page = page.ContactPage(self.driver)
        time.sleep(0.3)
        self.assertTrue(self.contact_page.populate_required_fields(forename="   "))
        self.assertFalse(self.contact_page.validate_form_errors("forename"))
        self.assertTrue(self.contact_page.populate_required_fields(email="++.com"))
        self.assertFalse(self.contact_page.validate_form_errors("email"))
        self.assertTrue(self.contact_page.populate_required_fields(msg="   "))
        self.assertFalse(self.contact_page.validate_form_errors("msg"))
        self.assertTrue(self._wait_for_warning_header("but we won't get it unless" \
                                                      "you complete the form correctly"))

    def test_case_4(self):
        """
        Test for shopping page and cart
        """
        print("Step: {} - {}".format(self._testMethodName, self._testMethodDoc))
        self.assertTrue(self.main_page.go_home_page())
        self.assertTrue(self.main_page.go_shop_page())
        self.shop_page = page.ShopPage(self.driver)
        time.sleep(0.3)
        items_to_buy = {"Funny Cow":2, "Fluffy Bunny":1}
        products_loc = self.shop_page.find_item_locators(items_to_buy)
        self.assertTrue(self.shop_page.click_buy_product(products_loc, items_to_buy))
        self.assertTrue(self.main_page.go_cart_page())
        time.sleep(0.3)
        self.cart_page = page.CartPage(self.driver)
        cart_loc = self.cart_page.find_cart_item_locators(items_to_buy)
        self.assertTrue(self.cart_page.compare_product_quantity(cart_loc, items_to_buy))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
