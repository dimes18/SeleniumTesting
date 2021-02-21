# Running the Test cases

### Activate venv
	C:\Selenium\SeleniumTesting\.venv\Scripts>activate
	(.venv) C:\Selenium\SeleniumTesting\

### Run all Test Cases in Pytest
```
(.venv) C:\Selenium\SeleniumTesting>pytest tests\test_pages.py -v
==================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.4.4, pytest-4.6.11, py-1.10.0, pluggy-0.13.1 -- c:\selenium\seleniumtesting\.venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Selenium\SeleniumTesting
collected 4 items                                                                                                                                                                            

tests/test_pages.py::PlanitTesting::test_case_1 PASSED                                                                                                                                 [ 25%]
tests/test_pages.py::PlanitTesting::test_case_2 PASSED                                                                                                                                 [ 50%]
tests/test_pages.py::PlanitTesting::test_case_3 PASSED                                                                                                                                 [ 75%]
tests/test_pages.py::PlanitTesting::test_case_4 PASSED                                                                                                                                 [100%]

================================================================================= 4 passed in 93.66 seconds =================================================================================

```


### Run Selected Test Case only
```
(.venv) C:\Selenium\SeleniumTesting>pytest tests\test_pages.py -v -k "test_case_4"
==================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.4.4, pytest-4.6.11, py-1.10.0, pluggy-0.13.1 -- c:\selenium\seleniumtesting\.venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Selenium\SeleniumTesting
collected 4 items / 3 deselected / 1 selected                                                                                                                                                

tests/test_pages.py::PlanitTesting::test_case_4 PASSED                                                                                                                                 [100%]

========================================================================== 1 passed, 3 deselected in 18.55 seconds ==========================================================================
```

### Excluding a specific test
```
(.venv) C:\Selenium\SeleniumTesting>pytest tests\test_pages.py -v -k "not case_3 and not case_4"
==================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.4.4, pytest-4.6.11, py-1.10.0, pluggy-0.13.1 -- c:\selenium\seleniumtesting\.venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Selenium\SeleniumTesting
collected 4 items / 2 deselected / 2 selected                                                                                                                                                

tests/test_pages.py::PlanitTesting::test_case_1 PASSED                                                                                                                                 [ 50%]
tests/test_pages.py::PlanitTesting::test_case_2 PASSED                                                                                                                                 [100%]

========================================================================== 2 passed, 2 deselected in 57.02 seconds ==========================================================================
    
```