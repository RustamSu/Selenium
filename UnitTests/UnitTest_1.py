import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# *************************************************
# Testing Chrome
# *************************************************


class ChromeWindow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_window_chrome_max(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        try:
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
            print('OK Main page loaded maximized', driver.name)
        except TimeoutException:
            print('Warning! Too mach time to load max', driver.name)
            driver.get_screenshot_as_file('Load_main_page_mach_time_maximazed' + driver.name + '.png')
        sleep(2)

    def test_window_chrome_1120x550(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        driver.set_window_size(1120, 550)
        try:
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
            print('OK Main page loaded 1120x550', driver.name)
        except TimeoutException:
            print('Warning! Too mach time to load 1120x550', driver.name)
            driver.get_screenshot_as_file('Load_main_page_mach_time_1120x550' + driver.name + '.png')
        sleep(2)

    def test_chrome(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        try:
            WebDriverWait(driver, 3). \
                until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))  # button Submit
            print('OK Main page loaded maximized', driver.name)
        except TimeoutException:
            print('Warning! Too mach time to load maximized', driver.name)
            driver.get_screenshot_as_file('Load_main_page_mach_time_maximized ' + driver.name + '.png')
        self.assertIn('California Real Estate – QA at Silicon Valley Real Estate', driver.title)
        print(driver.title, 'page was loaded')
        elem = driver.find_element(By.XPATH, "//input[@id='g2-name']")
        elem.clear()
        elem.send_keys('test_name')
        elem = driver.find_element(By.XPATH, "//input[@id='g2-email']")
        elem.clear()
        elem.send_keys('test_email@gmail.com')
        elem = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        elem.clear()
        elem.send_keys('test_memo')
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        sleep(3)
        driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").click()
        try:
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").send_keys('\n')
        except TimeoutException:
            print('No GO BACK!')
            driver.quit()
        sleep(2)
        WebDriverWait(driver, 5). \
            until(EC.visibility_of_all_elements_located((By.XPATH, "//img[contains(@class,'wp-image')]")))
        self.assertIn('California Real Estate – QA at Silicon Valley Real Estate', driver.title)
        print(driver.title, 'page was loaded End TestCase')

    @classmethod  # важно
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    ChromeWindow.main()
