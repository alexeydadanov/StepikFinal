import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru, es...etc")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome ")
    yield browser
    print("\nquit browser..")
    browser.quit()
