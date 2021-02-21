import pytest
import requests

@pytest.fixture()
def google():
    return requests.get("https://www.google.com")


class TestGoogle:

    def test_alive(self, google):
        assert google.status_code == 200

if __name__ == "__main__":
    pytest.main(['C:\\Selenium\\SeleniumTesting\\tests\\test_google.py'])