from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pathlib
import requests

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
            print("Error: {}".format(err))
        return False

    def get_value(self, xpath, property=None):
        assert self.status, "No Active browser!"
        assert xpath is not None, "Xpath cannot be empty!"
        try:
            obj = self.webpagedriver.find_element_by_xpath(xpath)
            if property:
                return obj.get_property(property)
            return obj.text
        except Exception as err:
            print("Error: {}".format(err))
        return None


if __name__ == "__main__":
    contact_page = '//*[@id="nav-contact"]/a'
    xp_brand = '/html/body/div[1]/div/div/a[2]'
    firefoxcrawler = WebCrawler("Firefox", "C:\\Selenium\\SeleniumTesting\\geckodriver.exe")
    if firefoxcrawler.open_url("http://jupiter.cloud.planittesting.com"):
        brand = firefoxcrawler.get_value(xp_brand)
        print(brand)
        if firefoxcrawler.set_action(contact_page):
            print("Contacts page")
        pass
