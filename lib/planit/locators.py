from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPageLocators(object):
    HOME_LINK = (By.ID, 'nav-home')
    CONTACT_LINK = (By.ID, 'nav-contact')
    TITLE = (By.CSS_SELECTOR, "head>title")

    SUCCESS_MSG = {"message": (By.CSS_SELECTOR, '.alert'),
                "back_button": (By.CSS_SELECTOR, 'a.btn:nth-child(2)')}

class ContactPageLocators(object):
    GO_BUTTON = (By.CSS_SELECTOR, ".btn-contact")
    FORM_FIELDS = {"forename": (By.CSS_SELECTOR, 'input#forename'),
                   "email": (By.CSS_SELECTOR, 'input#email'),
                   "msg": (By.CSS_SELECTOR, 'textarea#message')}
    
    FORM_WARNINGS = {"forename": (By.ID, 'forename-err'),
                   "email": (By.ID, 'email-err'),
                   "msg": (By.ID, 'message-err'),
                   "header": (By.ID, "header-message")}

class ShopPageLocators(object):
    pass

class KeyboardKeys(Keys):
    pass