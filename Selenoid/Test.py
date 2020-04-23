import random
import unittest
from time import sleep

import selenium.common.exceptions as Ex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from BrowserStack import helpers as h

capabilities = {
    "browserName": "chrome",
    "version": "80.0",
    "enableVNC": True,
    "enableVideo": False
}
driverw = webdriver.Remote(
    command_executor=h.command_exec,  # Сервак не мой, я только разместил объявление
    desired_capabilities=capabilities)


class FillFormUnitTestWinChrome(unittest.TestCase):

    def setUp(self):
        # url = h.command_execRad
        # self.driver = webdriver.Remote(command_executor=url,desired_capabilities=des_cap.desired_caps[0])
        self.driver = driverw
        # выбираем вариант оболочки из des_cap.py
        # self.driver = webdriver.Chrome()

    def test_fill_form(self):
        driver = self.driver
        driver.get(h.form_url)
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, h.XNameForm)))
            print('Go!', driver.name)
        except Ex.TimeoutException:
            print('Warning! Too mach time to load page', driver.name)
            driver.get_screenshot_as_file('Load_main_page_mach_time' + driver.name + '.png')
            driver.quit()

        try:
            driver.find_element_by_xpath(h.XFirstName).send_keys('Aleksandr')
            driver.find_element_by_xpath(h.XLastName).send_keys('Kuzhelev')
            driver.find_element_by_xpath(h.XEmail).send_keys(str(random.randrange(1000, 9999)) + '@gmail.com')
            driver.find_element_by_xpath(h.XPhone).send_keys(str(random.randrange(1, 9999999999)).zfill(10))
            print('First Name ok', '\n', 'Last Name ok', '\n', 'e-mail ok', '\n', 'phone ok')
        except Ex.ElementNotVisibleException:
            print("Warning! Don't see elements", driver.name)
            driver.get_screenshot_as_file('Text fields not visible' + driver.name + '.png')
            driver.quit()

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        try:
            driver.find_element(By.XPATH, "//label[@id='radio-0000000e" + str(random.randint(0, 5)) + "']").click()
            print('Radio ok')
        except Ex.ElementClickInterceptedException:
            print("Warning! Radio is not selectable", driver.name)
            driver.get_screenshot_as_file('Radio error' + driver.name + '.png')
            driver.quit()

        driver.find_element_by_xpath(h.XQuantity).send_keys(str(random.randint(1, 100)))  # quantity
        print('Quantity ok')

        try:
            driver.find_element_by_xpath(h.XCalendar).click()  # Вызываем календарь
            driver.implicitly_wait(5)
            driver.find_element_by_class_name("today ").click()
            print('Calendar ok')
        except Exception:
            print("Warning! Calendar is not selectable", driver.name)
            driver.get_screenshot_as_file('Calendar error' + driver.name + '.png')
            driver.quit()

        try:
            driver.find_element_by_xpath(h.XStreet1).send_keys('Lenin street')
            driver.find_element_by_xpath(h.XStreet2).send_keys('Marx street')
            driver.find_element_by_xpath(h.XCity).send_keys('Cinci')
            driver.find_element_by_xpath(h.XRegion).send_keys('OH')
            driver.find_element_by_xpath(h.XZipCode).send_keys('11111')
            driver.find_element_by_xpath(h.XCountry).click()
            driver.implicitly_wait(5)
            sleep(1)
            driver.find_element_by_xpath("//input[@placeholder='Country']").send_keys('Albania')
            # #самое очевидное решение для заполнения
            # driver.find_element_by_xpath(h.XSelCountry).click() # не работает в Safari
            # можно было в input толкать, но мы же эмулируем работу пользователя, так что жмем элемент из списка
            print('Street 1 ok', '\n', 'Street 2 ok', '\n', 'City', '\n', 'State ok', '\n', 'ZipCode ok', '\n',
                  'Country ok')
        except Exception:
            print("Text fields error", driver.name)
            driver.get_screenshot_as_file('Address fields error' + driver.name + '.png')
            driver.quit()

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        Select(driver.find_element_by_tag_name('select')).select_by_index(1)  # simple select
        print('Dropdown list ok')

        try:
            for i in range(3):
                if random.getrandbits(1):
                    driver.find_element(By.XPATH, "//label[@id='checkbox-00000018-" + str(i) + "']").click()

            driver.find_element(By.XPATH, "//label[@id='checkbox-00000018-3']").click()
            driver.find_element_by_xpath(h.XExtText).send_keys('blablabla')
            print('Checkbox ok')
        except Exception:
            print("Checkbox error", driver.name)
            driver.get_screenshot_as_file('Checkbox fields error' + driver.name + '.png')
            driver.quit()

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        # На capchа забьем, не всегда срабатывает
        # try:
        #     driver.execute_script(h.SolveCapcha())
        #     print('Capcha ok')
        # except Exception:
        #     print(Exception, 'Capcha was not solved')
        #     driver.quit()

        sleep(1)  # просто посмотреть на результат
        print('All OK!!!')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
