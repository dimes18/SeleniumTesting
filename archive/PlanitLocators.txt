from selenium.webdriver.common.by import By

class ContactPageLocators(object):    
    CONTACT_FORM = '/html/body/div[2]/div/form'        #--//form[@ng-model="formModel"]
    SUBMIT_BUTTON = '/html/body/div[2]/div/form/div/a' #--//button[@type="submit"]
    WARNINGS = {'alert':'//*[@id="header-message"]/div',
                'forename':'//*[@id="forename-err"]',
                'email':'//*[@id="email-err"]',
                'msgbox':'//*[@id="message-err"]'}
    INPUT_FIELDS = {'forename':'//*[@id="forename"]',
                    'surname':'//*[@id="surname"]',
                    'email':'//*[@id="email"]',
                    'telephone':'//*[@id="telephone"]',
                    'msgbox':'//*[@id="message"]'}
    INPUT_LABELS = {'forename':'/html/body/div[2]/div/form/fieldset/div[1]',
                    'surname':'/html/body/div[2]/div/form/fieldset/div[2]',
                    'email':'//*[@id="email-group"]',
                    'telephone':'//*[@id="telephone-group"]',
                    'msgbox':'//*[@id="message-group"]'}
    REQUIRED_INPUTS='//span[@class="req"]'

class MainPageLocators(object):
    BRAND = '/html/body/div[1]/div/div/a[2]'
    CONTACT_PAGE = '//*[@id="nav-contact"]/a'

class ElementLocators(object):
    HEADER_MSG = (By.ID, "header-message")