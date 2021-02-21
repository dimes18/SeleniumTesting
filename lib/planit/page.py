import time
from element import BasePageElement
from locators import *

class SearchTextElement(BasePageElement):
    pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

    wait_for_back_button = SearchTextElement(resource=MainPageLocators.SUCCESS_MSG['back_button'])
    wait_for_warning_header = SearchTextElement(resource=ContactPageLocators.FORM_WARNINGS['header'])
    wait_for_forename_err = SearchTextElement(resource=ContactPageLocators.FORM_WARNINGS['forename'])
    wait_for_email_err = SearchTextElement(resource=ContactPageLocators.FORM_WARNINGS['email'])
    wait_for_msg_err = SearchTextElement(resource=ContactPageLocators.FORM_WARNINGS['msg'])

class MainPage(BasePage):
    """Home Page methods"""

    def is_title_matches(self, keyword):
        """Verifies if keyword appears in page title"""
        return keyword in self.driver.title

    def click_home_page(self):
        try:
            element = self.driver.find_element(*MainPageLocators.HOME_LINK)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def click_contact_page(self):
        try:
            element = self.driver.find_element(*MainPageLocators.CONTACT_LINK)
            element.click()
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

class ContactPage(BasePage):
    """Contact Page methods"""

    def is_results_found(self):
        return "No results found." not in self.driver.page_source

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
        try:
            for key in kwargs:
                assert key in ContactPageLocators.FORM_FIELDS
                element = self.driver.find_element(*ContactPageLocators.FORM_FIELDS[key])
                element.send_keys(kwargs[key])
                element.send_keys(KeyboardKeys.TAB)
            return True
        except Exception as err:
            print("Error: {}".format(err))
        return False

    def validate_form_errors(self, *args):
        """check if no form errors"""        
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
    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source