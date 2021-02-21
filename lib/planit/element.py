from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement(object):

    def __init__(self, resource=None):
        self.locator = resource        

    def __set__(self, obj, value):
        try:
            driver = obj.driver
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element_by_name(self.locator))
            driver.find_element_by_name(self.locator).send_keys(value)
        except Exception as err:
            print("Error: {}".format(err))        

    def __get__(self, obj, owner):
        try:
            driver = obj.driver        
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element(*self.locator))
            element = driver.find_element(*self.locator)
            return element.get_attribute("innerText")
        except Exception as err:
            print("Error: {}".format(err))
        return ""