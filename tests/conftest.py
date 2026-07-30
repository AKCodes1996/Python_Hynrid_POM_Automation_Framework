import pytest
from selenium import  webdriver
from utilities import  read_Config

@pytest.fixture
def browser():

    url = read_Config.read_data("basic info","url")
    browser = read_Config.read_data("basic info","browser")
    if browser == "chrome":
        driver  = webdriver.Chrome()
    if browser == "Edge":
        driver = webdriver.Edge()

    driver.get(url)
    yield driver
    driver.quit()