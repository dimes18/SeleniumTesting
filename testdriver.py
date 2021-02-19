from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

#bin_arg = FirefoxBinary('%PROGRAMFILES%\Mozilla Firefox\firefox.exe')
capabilities_argument = DesiredCapabilities().FIREFOX
capabilities_argument["marionette"] = True
exe_path='C:\\Selenium\\SeleniumTesting\\geckodriver.exe'
webpagedriver = webdriver.Firefox(capabilities=capabilities_argument, executable_path=exe_path)

webpagedriver.get('http://jupiter.cloud.planittesting.com')
xp_brand = '/html/body/div[1]/div/div/a[2]'
obj = webpagedriver.find_element_by_xpath(xp_brand)
print("Brand: {}".format(obj.text))