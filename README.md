# SeleniumTesting
---
## Selenium Webdriver using Python
Platform: Windows 10 64bit, Language: Python 3.4

## Dependencies
### Install Selenium Webdriver
	- Install Java Software Development Kit (JDK)
	https://www.oracle.com/java/technologies/javase-jdk15-downloads.html
	- Install Selenium Webdriver for Python or Java Client Driver
	For Java - https://www.selenium.dev/downloads/
	For python - use pip install -U selenium
### Locate Firefox binary
	e.g. C:\Program Files\Mozilla Firefox

### Download geckodriver and copy to app folder
	https://github.com/mozilla/geckodriver/releases

### Install virtualenv
	pip install virtualenv 

### Create virtualenv (venv)
```
	- virtualenv -p python .venv
	C:\Selenium>virtualenv -p python .venv
	Running virtualenv with interpreter C:\Python34\python.exe
	Using base prefix 'C:\\Python34'
	New python executable in C:\Selenium\SeleniumTesting\.venv\Scripts\python.exe
	Installing setuptools, pip, wheel...
	done.
```

### Activate venv
	C:\Selenium\SeleniumTesting\.venv\Scripts>activate
### Install selenium in venv
```
	pip install -U selenium
	check installed package - 
	(.venv) C:\Selenium\SeleniumTesting\.venv\Lib>cd site-packages
	Directory of C:\Selenium\SeleniumTesting\.venv\Lib\site-packages
	19/02/2021  03:22 PM    <DIR>          selenium
	19/02/2021  03:22 PM    <DIR>          selenium-3.141.0.dist-info
```
### Verify installed selenium-web driver with python
* webpage: https://jupiter.cloud.planittesting.com

```
	(.venv) C:\Selenium\SeleniumTesting>.venv\Scripts\python testdriver.py
    Brand: Jupiter Toys
```