import pytest
import time
from lib.WebUI import WebCrawler

@pytest.fixture(scope="module")
def planit_firefox():
    webcrawler = WebCrawler("Firefox", "C:\\Selenium\\SeleniumTesting\\geckodriver.exe")
    webcrawler.open_url("http://jupiter.cloud.planittesting.com")
    time.sleep(5)
    return webcrawler

@pytest.fixture(autouse=True, scope="class")
def _load_planittesting_page(firefoxdriver, planit_firefox):
    firefoxdriver.cls._webpage = planit_firefox

class TestPlanitFirefox:
    CONTACT_PAGE = '//*[@id="nav-contact"]/a'
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

    # /html/body/div[2]/div/form/fieldset/div[1]/label        //*[@id="forename"]     /html/body/div[2]/div/form/fieldset/div[1]/div/input
    # /html/body/div[2]/div/form/fieldset/div[2]/label        //*[@id="surname"]      /html/body/div[2]/div/form/fieldset/div[2]/div/input

    #//*[@id="email-group"]/label/span
    #//span[@class='req']
    #//label[@class='control-label']

    def test_openurl_contact_page(self):
        self._webpage.set_action(self.CONTACT_PAGE)
        assert "form" in self._webpage.get_value(self.CONTACT_FORM, property="ng-model")
    
    def test_submit_blank_alert_warning(self):
        self._webpage.set_action(self.SUBMIT_BUTTON)
        time.sleep(1)
        assert "correctly" in self._webpage.get_value(self.WARNINGS['alert'])

    def test_submit_blank_forename_warnings(self):
        assert "required" in self._webpage.get_value(self.WARNINGS['forename'])

    def test_submit_blank_email_warning(self):
        assert "required" in self._webpage.get_value(self.WARNINGS['email'])

    def test_submit_blank_messagebox_warning(self):
        assert "required" in self._webpage.get_value(self.WARNINGS['msgbox'])

    def test_populate_mandatory_fields(self):        
        status = False
        required_fields = self._webpage.get_values(self.REQUIRED_INPUTS)
        try:      
            for xpath in required_fields:
                elem = self._webpage.find_element_by_xpath(xpath)
                if "name" in elem.text:
                    elem.send_keys("Johnny")
                elif "email" in elem.text:
                    elem.send_keys("Johnny@jmail.com")
                else:
                    elem.send_keys("Hello World!")
            status = True
        except Exception as err:
            pass
        assert status

    def test_submit_warnings_gone(self):
        status = True
        for key, xpath in self.WARNINGS:
            obj = self._webpage.get_value(xpath)
            if obj.text:
                status &= False
        assert status

if __name__ == "__main__":
    pytest.main(['C:\\Selenium\\SeleniumTesting\\tests\\test_cases.py'])
    