import pytest
from selenium import webdriver


class Test_Allure():
    @pytest.fixture()
    def test_setUp_tearDown(self):
        global driver
        # driver = self.driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        print('setUp')
        yield
        print('tearDown')
        driver.close()

    # @unittest.skip
    # @allure.feature('Open page')
    def test_qasv(self, test_setUp_tearDown):
        # driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        assert driver.title == 'California Real Estate – QA at Silicon Valley Real Estate'

    # @unittest.skip
    # @allure.feature('Open page')
    def test_Google(self, test_setUp_tearDown):
        # driver = self.driver
        driver.get("https://Google.com/")
        assert driver.title == 'Google'

    # @allure.feature('Open page')
    def test_Github(self, test_setUp_tearDown):
        # driver = self.driver
        driver.get("https://github.com")
        assert driver.title.index('GitHub') > -1  # in incognito is different title
