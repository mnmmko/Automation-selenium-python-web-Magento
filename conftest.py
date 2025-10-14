import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from common.DriveManeger import DriverManager


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = DriverManager.get_driver()
    url = "http://live.techpanda.org/index.php/"
    driver.maximize_window()
    driver.get(url)
    yield driver
    DriverManager.quit_driver()