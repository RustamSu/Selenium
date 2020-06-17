import pytest
from selenium import webdriver


def test_setUp():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    print('setUp')

def test_qasv():
    # driver = self.driver
    driver.get("https://qasvus.wordpress.com/")
    print('qasv')
    assert driver.title == 'California Real Estate – QA at Silicon Valley Real Estate'

def test_Google():
    # driver = self.driver
    driver.get("https://Google.com/")
    print('Google')
    assert driver.title == 'Google'

def test_Github():
    # driver = self.driver
    driver.get("https://github.com")
    print('GitHub')
    assert driver.title.index('GitHub') > -1  # in incognito is different title

def test_tearDown():
    driver.close()


