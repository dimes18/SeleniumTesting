"""
element.py: Implements descriptor class for page elements

__author__ = "Don Ariston Urbano"
__credits__ = ["https://selenium-python.readthedocs.io/index.html"]
"""

from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """ Base Page Element class for finding elements """
    def __init__(self, resource=None):
        self.locator = resource

    def __set__(self, obj, value):
        """ To set value to element. Obj is from the instantiating class that contains webdriver"""
        try:
            driver = obj.driver
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element_by_name(self.locator))
            driver.find_element_by_name(self.locator).send_keys(value)
        except Exception as err:
            print("Error: {}".format(err))

    def __get__(self, obj, owner):
        """ To get element value. Obj is from the instantiating class that contains webdriver"""
        try:
            driver = obj.driver
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element(*self.locator))
            element = driver.find_element(*self.locator)
            return element.get_attribute("innerText")
        except Exception as err:
            print("Error: {}".format(err))
        return ""
