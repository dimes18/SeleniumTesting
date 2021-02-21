from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from lib.PlanitLocators import ElementLocators

import time
import pathlib
import requests

class SearchTypes(By):
    CLASS_NAME = "class_name"
    CSS_SELECTOR = "css_selector"
    ID = "id"
    LINK_TEXT = "link_text"
    NAME = "name"
    PARTIAL_LINK_TEXT = "partial_link_text"
    TAG_NAME = "tag_name"
    XPATH = "xpath"

class WebCrawler():

    def __init__(self, webbrowser, driverpath):
        assert webbrowser is not None, "Provide a valid Web Browser name!"
        assert pathlib.Path(driverpath).exists(), "Provide a valid web Driver!"

        self.browsertype = None
        self.func = None
        self.webpagedriver = None
        self.driver = driverpath
        self.browser = webbrowser.upper()
        self.status = False
        try:
            if hasattr(DesiredCapabilities(), self.browser):
                self.browsertype = getattr(DesiredCapabilities(), self.browser)
                self.browsertype["marionette"] = True
                self.func = getattr(webdriver, self.browser.capitalize())
                self.webpagedriver = self.func(capabilities=self.browsertype,
                                               executable_path=self.driver)
                self.status = True
            else:
                print("Unsupported Browser!")
        except Exception as err:
            print("Error: {}".format(err))

    def open_url(self, url):
        try:
            resp = requests.head(url)
            assert resp.status_code < 400, "Provide a valid URL!"
            self.webpagedriver.get(url)
            self.status = True
            return self.status
        except AssertionError as err:
            print("URL Error: {}".format(err))
            self.status = False
        except Exception as err:
            print("WebDriver Error: {}".format(err))
            self.status = False
        return self.status

    def set_action(self, xpath):
        assert self.status, "No Active browser!"
        assert xpath is not None, "Xpath cannot be empty!"
        obj = self.webpagedriver.find_element_by_xpath(xpath)
        time.sleep(1)
        try:
            obj.click()
            return True
        except Exception as err:
            print("Error setting action: {}".format(err))
        return False

    def get_element(self, entity, searchtype, property=None, instance=False):
        assert hasattr(By, searchtype.upper()), "Not Valid Search Type!"
        assert entity is not None, "Provide a valid element entity!"
        func = None
        if hasattr(self.webpagedriver, "find_element_by_{}".format(searchtype)):
            try:
                func = getattr(self.webpagedriver, "find_element_by_{}".format(searchtype))
                object_element = func(entity)
                if instance:
                    return object_element
                if property:                    
                    return object_element.get_property(property)                
                return object_element.text
            except Exception as err:
                print("Error getting element: {}".format(err))
        else:
            print("Error Searchtype invalid:")
        return None

    def get_elements(self, entity, searchtype, property=None, instances=False):
        assert hasattr(By, searchtype.upper()), "Not Valid Search Type!"
        assert entity is not None, "Provide a valid element entity!"
        values = []
        func = None
        if hasattr(self.webpagedriver, "find_elements_by_{}".format(searchtype)):
            try:
                func = getattr(self.webpagedriver, "find_elements_by_{}".format(searchtype))
                object_elements = func(entity)
                if instances:
                    return object_elements                
                for obj in object_elements:
                    if property:
                        values.append(obj.get_property(property))
                    values.append(obj.text)
                return values
            except Exception as err:
                print("Error getting element: {}".format(err))
        else:
            print("Error Searchtype invalid:")
        return None

    @staticmethod
    def slow_typing(element, input):
        for char in input: 
            element.send_keys(char)
            time.sleep(0.4)


if __name__ == "__main__":
    contact_page = '//*[@id="nav-contact"]/a'
    xp_brand = '/html/body/div[1]/div/div/a[2]'
    firefoxcrawler = WebCrawler("Firefox", "C:\\Selenium\\SeleniumTesting\\geckodriver.exe")
    if firefoxcrawler.open_url("http://jupiter.cloud.planittesting.com"):
        """
        brand = firefoxcrawler.get_xpath_value(xp_brand)
        print(brand)
        if firefoxcrawler.set_action(contact_page):
            print("Contacts page")
        pass
        """
        brand = firefoxcrawler.get_element("brand", SearchTypes.CLASS_NAME)
        print(brand)
        if firefoxcrawler.set_action(contact_page):
            header_message = firefoxcrawler.webpagedriver.find_element(ElementLocators.HEADER_MSG)
            print(header_message)

            #return required fields
            req_flds = firefoxcrawler.get_elements(".control-group", SearchTypes.CSS_SELECTOR)
        pass
            