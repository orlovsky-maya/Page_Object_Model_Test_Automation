# My environment: Ubuntu 22.04.2 LTS, 64-bit
# Chromium Version 113.0.5672.63 (Official Build) snap (64-bit)
# Firefox 113.0.1 (64-bit)


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utilities.Logger import Logger


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options()
        chrome_options.add_argument("--remote-debugging-port=9515")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def logger(request):
    logger = Logger(request.config.rootdir)
    return logger
