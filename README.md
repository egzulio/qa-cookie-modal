# Simple cookie modal automation in Playwright + pytest

The project aims to provide simple automation in the cookie modal and verify that the analytic cookie has been added to the browser. The test was created in accordance with the Page Object Model to be fully reusable in the future.


## Structure
```bash
qa-cookie-modal/
├── pages/                # folder with Page Object classes
│   ├── __init__.py       # file initiating module pages
│   └── cookie_modal.py   # Page Object for cookie modal
├── tests/                # Folder with test files
│   └── test_cookies.py   # Test file
├── conftest.py           # Fixture and config pytest
├── requirements.txt      # Requirements list file
├── playwright.yml        # GitHub Actions workflow configuration
└── .gitignore            # File with elements to be ignore in git  
```  
## File description

```bash
cookie_modal.py - The file contains the POM for the cookie modal
```

```bash
conftest.py - Contains fixtures for clearing cookies before each test
```

```bash
test_cookies.py - Contains test for analytic cookie and verifies that the cookie was added with the appropriate value
```
```bash
playwright.yml  - The workflow file configures Playwright tests to run automatically on every push or pull request, across Chromium, Firefox, and WebKit browsers. Tests are run in parallel thanks to the matrix strategy.
```
## Installation

1. Create and activate virtual environment

```bash
    python3 -m venv myenv
    source myenv/bin/activate  # Linux/macOS
    myenv\Scripts\activate     # Windows
```

2. Install dependencies

```bash
    pip install -r requirements.txt
```

3. Install browsers

```bash
    python -m playwright install
```


    
## Running Tests

To run tests, run the following command

```bash
    pytest tests/test_cookies.py # Windows
    python -m pytest tests/cookies_test.py #Linux/macOS
```
To run tests with a visible browser window (headed):

```bash
    pytest --headed tests/test_cookies.py # Windows 
    python -m pytest --headed tests/cookies_test.py # Linux/macOS
```
To run tests on multiple browsers:

```bash
    pytest --browser firefox --browser webkit tests/test_cookies.py # Windows 
    python -m pytest --browser firefox --browser webkit  tests/cookies_test.py # Linux/macOS
```
To repeat tests multiple times (e.g., 5 times):

```bash
    pytest tests/test_cookies.py --count=5 # Windows
    python -m pytest tests/cookies_test.py --count=5 #Linux/macOS
```



## Authors

Michał Dylewicz 

[Linkedin](https://www.linkedin.com/in/michal-dylewicz/) - dylewicz.michal@gmail.com

Project Link: [https://github.com/egzulio/qa-cookie-modal](https://github.com/egzulio/qa-cookie-modal)

