# My environment: Ubuntu 22.04.2 LTS, 64-bit
# Chromium Version 113.0.5672.63 (Official Build) snap (64-bit)
# Firefox 113.0.1 (64-bit)


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language, example: fr, ru or es")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_data_dir', action='store', default=None,
                     help="Enter user directory for browser")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    browser_name = request.config.getoption("browser_name")

    user_data_dir = request.config.getoption('user_data_dir')

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
        chrome_options.add_argument("--remote-debugging-port=9515")
        if user_data_dir:
            chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
