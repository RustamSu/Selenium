import unittest
from time import sleep

import HtmlTestRunner
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ChromeFillForm(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # запускаем один раз, а не перед каждым тестом
        cls.driver.maximize_window()
        cls.driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")

    def test_contains_elements(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//h1[contains(text(),'Online Quiz')]")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//p[contains(text(),'Please answer the Online Quiz below. You will rece')]")))
        for i in range(0, 2):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='00000008_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'What is the longest river in the world?')]")))
        for i in range(0, 2):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='0000000a_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'Which of the following inventions occured in the 17th century?')]")))
        for i in range(0, 4):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='0000000c_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'What name is given to the programs ran by a computer')]")))
        for i in range(0, 3):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='0000000e_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'What food group has the highest level')]")))
        for i in range(0, 2):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='00000010_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[text()='Your Email']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

    def test_clickable_elements(self):
        driver = self.driver
        for i in range(0, 2):  # radio animal
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000008_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000008_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 2):  # radio river
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000a_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000a_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 4):  # checkbox inventions
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000c_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000c_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 3):  # checkbox program
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000e_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000e_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 2):  # checkbox food
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000010_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000010_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys('sss@sss.com')
        driver.find_element_by_tag_name('html').send_keys(Keys.TAB)

    def test_negative_email(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).clear()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys('ssssss.com')
        driver.find_element_by_tag_name('html').send_keys(Keys.TAB)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//label[@id='email-00000018-error-acc']")))

    def test_images_for_200_response(self):  # Проверка на то что все картинки нормально загрузились
        driver = self.driver
        example_images = driver.find_elements(By.TAG_NAME, 'img')
        for image in example_images:
            current_link = image.get_attribute("src")
            r = requests.get(current_link)
            try:
                self.assertEqual(r.status_code, 200)
                # print(current_link,'is loaded')
            except AssertionError:
                self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)

    def test_social_button(self):
        driver = self.driver
        # tests other social-net buttons
        soc_net = ['twitter', 'linkedin', 'google-plus']
        for s in soc_net:
            driver.find_element(By.XPATH, "//a[@data-button-type='" + s + "']").click()
            driver.switch_to.window(driver.window_handles[1])
            sleep(1)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        driver.implicitly_wait(3)
        # test fasebook
        driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='fb-like fb_iframe_widget']//iframe"))
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "//button[@title='Like']").click()

    @classmethod  # важно
    def tearDownClass(cls):
        cls.driver.quit()


class FireFoxFillForm(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()  # запускаем один раз, а не перед каждым тестом
        cls.driver.maximize_window()
        cls.driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")

    def test_contains_elements(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//h1[contains(text(),'Online Quiz')]")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//p[contains(text(),'Please answer the Online Quiz below. You will rece')]")))
        for i in range(0, 2):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='00000008_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'What is the longest river in the world?')]")))
        for i in range(0, 2):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='0000000a_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'Which of the following inventions occured in the 17th century?')]")))
        for i in range(0, 4):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='0000000c_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'What name is given to the programs ran by a computer')]")))
        for i in range(0, 3):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='0000000e_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[contains(text(),'What food group has the highest level')]")))
        for i in range(0, 2):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//input[@id='00000010_" + str(i) + "']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                         "//label[text()='Your Email']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

    def test_clickable_elements(self):
        driver = self.driver
        for i in range(0, 2):  # radio animal
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000008_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000008_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 2):  # radio river
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000a_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000a_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 4):  # checkbox inventions
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000c_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000c_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 3):  # checkbox program
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000e_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='0000000e_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        for i in range(0, 2):  # checkbox food
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000010_" + str(
                                                                                 i) + "']"))).click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//label[@for='00000010_" + str(
                                                                                 i) + "' and @aria-checked='true']")))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys('sss@sss.com')
        driver.find_element_by_tag_name('html').send_keys(Keys.TAB)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys('')

    def test_negative_email(self):
        driver = self.driver
        sleep(3)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).clear()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys('ssssss.com')
        driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
        sleep(2)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//label[@id='email-00000018-error-acc']")))

    def test_images_for_200_response(self):  # Проверка на то что все картинки нормально загрузились
        driver = self.driver
        example_images = driver.find_elements(By.TAG_NAME, 'img')
        for image in example_images:
            current_link = image.get_attribute("src")
            r = requests.get(current_link)
            try:
                self.assertEqual(r.status_code, 200)
                # print(current_link,'is loaded')
            except AssertionError:
                self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)

    @classmethod  # важно
    def tearDownClass(cls):
        cls.driver.quit()


class FireFoxFacebookButton(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()  # запускаем один раз, а не перед каждым тестом
        cls.driver.maximize_window()
        cls.driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")

    def test_facebook_button(self):
        driver = self.driver
        # test facebook
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='fb-like fb_iframe_widget']//iframe"))
        driver.implicitly_wait(3)
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Like']")))
        element.click()

    @classmethod  # важно
    def tearDownClass(cls):
        cls.driver.quit()


class FireFoxSocialNetButton(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()  # запускаем один раз, а не перед каждым тестом
        cls.driver.maximize_window()
        cls.driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")

    def test_social_button(self):
        driver = self.driver
        sleep(2)
        # tests other social-net buttons
        soc_net = ['twitter', 'linkedin', 'google-plus']
        for s in soc_net:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-button-type='" + s + "']")))
            element.location_once_scrolled_into_view
            element.click()
            sleep(3)
            # print(s, driver.window_handles)
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod  # важно
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='d:/Documents/GitHub/Selenium/ReportsH''/HtmlReports'))
