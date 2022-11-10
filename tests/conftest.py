import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("D:\\Course\\Selenium\\Drivers\\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox":
        service_obj = Service("D:\\Course\\Selenium\\Drivers\\geckodriver.exe")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=service_obj, options=firefox_options)
    elif browser_name == "IE":
        service_obj = Service("D:\\Course\\Selenium\\Drivers\\msedgedriver.exe")
        ie_options = webdriver.EdgeOptions()
        ie_options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=service_obj, options=ie_options)

    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.close()
    return driver
