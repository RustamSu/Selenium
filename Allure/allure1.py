import unittest
import allure

from selenium import webdriver


class ChromeWindow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # @unittest.skip
    @allure.feature('Open page')
    def test_qasv(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        assert driver.title == 'California Real Estate – QA at Silicon Valley Real Estate'

    # @unittest.skip
    @allure.feature('Open page')
    def test_Google(self):
        driver = self.driver
        driver.get("https://Google.com/")
        assert driver.title == 'Google'

    @allure.feature('Open page')
    def test_Github(self):
        driver = self.driver
        driver.get("https://github.com")
        assert driver.title.index('GitHub') > -1  # in incognito is different title

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    ChromeWindow.main()
