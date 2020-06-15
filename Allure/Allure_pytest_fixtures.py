import pytest
import allure
from selenium import webdriver



@pytest.fixture()
def test_setUp_tearDown():
    global driver
    # driver = self.driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    print('setUp')
    yield
    print('tearDown')
    driver.close()

def test_qasv(test_setUp_tearDown):
    # driver = self.driver
    driver.get("https://qasvus.wordpress.com/")
    assert driver.title == 'California Real Estate – QA at Silicon Valley Real Estate'

def test_Google(test_setUp_tearDown):
    # driver = self.driver
    driver.get("https://Google.com/")
    assert driver.title == 'Google'

def test_Github(test_setUp_tearDown):
    # driver = self.driver
    driver.get("https://github.com")
    assert driver.title.index('GitHub') > -1  # in incognito is different title


