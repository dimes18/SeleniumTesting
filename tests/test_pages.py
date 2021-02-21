import unittest
#import pytest
import time
from selenium import webdriver
from lib.planit import page


class PlanitTesting(unittest.TestCase):
    """Class for testing Planit test webpage"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_page = None
        self.contact_page = None

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
        self.assertTrue(self.main_page.click_home_page())
        self.assertTrue(self.main_page.click_contact_page())
        self.contact_page = page.ContactPage(self.driver)
        time.sleep(0.3)
        self.assertTrue(self.contact_page.click_go_button())
        self.assertFalse(self.contact_page.validate_form_errors("forename", "email", "msg" ))
        self.assertTrue(self.contact_page.populate_required_fields(forename="Johnny", email="Johnny@jmail.com",msg="Thank you!"))
        self.assertTrue(self.contact_page.validate_form_errors("forename", "email", "msg" ))
        self.assertTrue(self._wait_for_warning_header("tell it how it is"))

    def test_case_2(self):
        """
        Test for submit form submission is successful
        """
        print("Step: {} - {}".format(self._testMethodName, self._testMethodDoc))
        self.assertTrue(self.main_page.click_home_page())
        self.assertTrue(self.main_page.click_contact_page())
        self.contact_page = page.ContactPage(self.driver)
        time.sleep(0.3)
        self.assertTrue(self.contact_page.populate_required_fields(forename="Jonny", email="Jonny@jmail.com",msg="Cheers!"))
        self.assertTrue(self.contact_page.click_go_button())
        self.assertTrue(self._wait_for_back_button())
        self.assertIn("Thanks", self.contact_page.validate_submission_message())

    def test_case_3(self):
        """
        Test for submit form with invalid inputs
        """
        print("Step: {} - {}".format(self._testMethodName, self._testMethodDoc))
        self.assertTrue(self.main_page.click_home_page())
        self.assertTrue(self.main_page.click_contact_page())
        self.contact_page = page.ContactPage(self.driver)
        time.sleep(0.3)
        self.assertTrue(self.contact_page.populate_required_fields(forename="   "))        
        self.assertFalse(self.contact_page.validate_form_errors("forename"))
        self.assertTrue(self.contact_page.populate_required_fields(email="++.com"))        
        self.assertFalse(self.contact_page.validate_form_errors("email"))
        self.assertTrue(self.contact_page.populate_required_fields(msg="   "))        
        self.assertFalse(self.contact_page.validate_form_errors("msg"))
        self.assertTrue(self._wait_for_warning_header("but we won't get it unless you complete the form correctly"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    #pytest.main()