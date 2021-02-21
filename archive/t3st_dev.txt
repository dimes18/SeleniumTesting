import pytest
import requests

"""
@pytest.fixture(scope='module')
def google():
    return requests.get("https://www.google.com")


@pytest.fixture(autouse=True, scope='class')
def _request_google_page(request, google):
    request.cls._response = google


class TestGoogle:

    def test_alive(self):
        assert self._response.status_code == 200
"""
@pytest.fixture(scope="class")
def google(request):
    request.cls.google = requests.get("https://www.google.com")


@pytest.mark.usefixtures("google")
class TestGoogle:
    def test_alive(self):
        assert self.google.status_code == 200

if __name__ == "__main__":
    pytest.main(['C:\\Selenium\\SeleniumTesting\\tests\\test_newgoogle.py'])