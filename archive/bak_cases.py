import pytest
from lib.WebUI import WebCrawler

@pytest.fixture
def firefoxbrowser():
    contact_page = '//*[@id="nav-contact"]/a'
    contact_form = '/html/body/div[2]/div/form'
    submit_button = '/html/body/div[2]/div/form/div/a'
    status_label = '//*[@id="header-message"]/div'
    return WebCrawler("Firefox", "C:\\Selenium\\SeleniumTesting\\geckodriver.exe")

@pytest.fixture
def loadpage(firefoxbrowser):
    firefoxbrowser.open_url('http://jupiter.cloud.planittesting.com')
    return firefoxbrowser


def test_contact_page():
    pass