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
            print("Error setting action: {}".format(err))
        return False

    def get_value(self, xpath, property=None):
        #assert self.status, "No Active browser!"
        assert xpath is not None, "Xpath cannot be empty!"
        try:
            obj = self.webpagedriver.find_element_by_xpath(xpath)
            if property:
                return obj.get_property(property)
            return obj.text
        except Exception as err:
            print("Error getting value: {}".format(err))
        return None
    
    def get_values(self, xpath):
        #assert self.status, "No Active browser!"
        assert xpath is not None, "Xpath cannot be empty!"
        values = []
        try:
            object_elements = self.webpagedriver.find_elements_by_xpath(xpath)
            for o in object_elements:
                values.append(o.text)
            return values
        except Exception as err:
            print("Error getting elements: {}".format(err))
        return None

    def get_form_inputs(self, count, label_xpath, input_xpath, mandatory=False):
        #assert self.status, "No Active browser!"
        assert label_xpath is not None, "Label Xpath cannot be empty!"
        assert input_xpath is not None, "Input Xpath cannot be empty!"
        labelxpaths = []
        inputxpaths = []
        try:
            for idx in range(count):
                if mandatory:
                    if "*" in self.get_value("{}[{}]/label".format(label_xpath, str(idx))):                        
                        labelxpaths.append("{}[{}]/label".format(label_xpath, str(idx)))
                        inputxpaths.append("{}[{}]/label".format(input_xpath, str(idx)))
                    else:
                        continue
                else:
                    labelxpaths.append("{}[{}]/label".format(label_xpath, str(idx)))
                    inputxpaths.append("{}[{}]/label".format(input_xpath, str(idx)))
            return labelxpaths, inputxpaths
        except Exception as err:
            print("Error getting form inputs: {}".format(err))
        return None, None

    def fill_form_inputs(self, values, input_xpaths, mandatory=False):        
        assert len(input_xpaths) < 1, "Input Xpath cannot be empty!"
        assert len(values) != len(input_xpaths), "Input values and xpaths must tally!"
        count = 0
        try:
            for idx, xpath in enumerate(input_xpaths):
                try:
                    element = self.webpagedriver.find_element_by_xpath(xpath)
                    element.send_keys(values[idx])
                    count+=1
                except Exception as err:
                    print("Error accessing input element: {}".format(err))
            if count == len(values):
                return True
            return False
        except Exception as err:
            print("Error form inputs: {}".format(err))
        return False

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
