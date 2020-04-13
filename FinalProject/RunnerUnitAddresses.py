import unittest
from time import sleep

import HtmlTestRunner
import helper as h
from selenium import webdriver
from selenium.webdriver.common.by import By

#import KillProcess


class ChromeAuthorization(unittest.TestCase):

    @classmethod  # важно
    def authorize(cls, account):  # Варианты авторизации ['Facebook','Google','Email']
        driver = cls.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        sleep(3)
        type_login = ['Facebook', 'Google', 'Email']
        if account == 'Email':
            driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
            driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
        elif account == 'Google':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="ggl-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(h.google_email)
            driver.find_element(By.XPATH, '//div[@id="identifierNext"]').click()
            sleep(2)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(h.google_pasw)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//div[@id="passwordNext"]').click()
            driver.switch_to.window(driver.window_handles[0])
        elif account == 'Facebook':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="fb-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(h.fb_email)
            driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(h.fb_pass)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@name="login"]').click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod  # важно
    def setUpClass(cls):
        # KillProcess.killproc('chromedriver.exe')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://qasvus.wixsite.com/ca-marketing")
        sleep(5)
        cls.authorize('Email')  # Варианты авторизации ['Facebook','Google','Email']
        sleep(3)

    def test_auth(self):
        driver = self.driver
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"Log Out")]').click()
        sleep(5)
        self.authorize('Google')
        driver = self.driver
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"Log Out")]').click()
        sleep(5)
        self.authorize('Facebook')
        driver = self.driver
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"Log Out")]').click()
        sleep(5)
        self.authorize('Email')

    @classmethod  # важно
    def tearDown(cls):
        cls.driver.quit()


class ChromeNewAddresses(unittest.TestCase):

    @classmethod  # важно
    def authorize(cls, account):  # Варианты авторизации ['Facebook','Google','Email']
        driver = cls.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        sleep(3)
        type_login = ['Facebook', 'Google', 'Email']
        if account == 'Email':
            driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
            driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
            driver.implicitly_wait(5)
        elif account == 'Google':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="ggl-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(h.google_email)
            driver.find_element(By.XPATH, '//div[@id="identifierNext"]').click()
            sleep(2)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(h.google_pasw)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//div[@id="passwordNext"]').click()
            driver.switch_to.window(driver.window_handles[0])
        elif account == 'Facebook':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="fb-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(h.fb_email)
            driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(h.fb_pass)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@name="login"]').click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod  # важно
    def setUpClass(cls):
        #KillProcess.killproc('chromedriver.exe')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://qasvus.wixsite.com/ca-marketing")
        sleep(5)
        cls.authorize('Email')  # Варианты авторизации ['Facebook','Google','Email']
        sleep(5)

    def test_new_address(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing/account/my-addresses")
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"My Addresses")]').click()
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="My Addresses"]'))
        driver.find_element(By.XPATH, '//div[@id="root"]/div/main/section/div[3]/button').click()  # Add new Address

        sleep(5)
        driver.switch_to.default_content()
        fr = driver.find_elements(By.TAG_NAME, "iframe")  # это тоже работает
        for i in fr:
            if i.get_attribute('id')[:8] == 'tpaPopup':
                f = i
        print(f.get_attribute('id'))
        driver.switch_to.frame(f)

        # driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[contains(@id,"tpaPopup")]')) # и так тоже работает
        driver.implicitly_wait(5)

        driver.find_element(By.ID, "firstName-field").click()
        driver.find_element(By.ID, "firstName-field").send_keys('firstName')
        driver.find_element(By.ID, "lastName-field").send_keys('lastName')
        driver.find_element(By.ID, "company-field").send_keys('NewCompany')
        driver.find_element(By.ID, "addressLine1-field").send_keys('addressLine1-field')
        driver.find_element(By.ID, "addressLine2-field").send_keys('addressLine2-field')
        driver.find_element(By.ID, "city-field").send_keys('city-field')
        driver.find_element(By.ID, "country-field").click()
        driver.find_element(By.XPATH, '//div[text()="Algeria"]').click()
        driver.find_element(By.ID, "zipCode-field").send_keys('12345')
        driver.find_element(By.ID, "phone-field").send_keys('1234567890')

        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Add Address")]').click()

    @classmethod  # важно
    def tearDown(self):
        self.driver.quit()


class ChromeEditAddresses(unittest.TestCase):
    @classmethod  # важно
    def authorize(cls, account):  # Варианты авторизации ['Facebook','Google','Email']
        driver = cls.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        sleep(3)
        type_login = ['Facebook', 'Google', 'Email']
        if account == 'Email':
            driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
            driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
            driver.implicitly_wait(5)
        elif account == 'Google':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="ggl-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(h.google_email)
            driver.find_element(By.XPATH, '//div[@id="identifierNext"]').click()
            sleep(2)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(h.google_pasw)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//div[@id="passwordNext"]').click()
            driver.switch_to.window(driver.window_handles[0])
        elif account == 'Facebook':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="fb-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(h.fb_email)
            driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(h.fb_pass)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@name="login"]').click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod  # важно
    def setUpClass(cls):
        #KillProcess.killproc('chromedriver.exe')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://qasvus.wixsite.com/ca-marketing")
        sleep(5)
        cls.authorize('Email')  # Варианты авторизации ['Facebook','Google','Email']
        sleep(5)

    def test_edit_address(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing/account/my-addresses")
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        print('press menu')
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"My Addresses")]').click()
        print('press my_address')
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="My Addresses"]'))
        print('switch iframe_MyAddress')
        sleep(3)
        driver.find_element(By.XPATH, '//div[@id="root"]/div/main/section/div/ul/li/div/div/div/div/button').click()
        print('click Edit')
        sleep(5)
        driver.switch_to.default_content()
        fr = driver.find_elements(By.TAG_NAME, "iframe")  # это тоже работает
        for i in fr:
            if i.get_attribute('id')[:8] == 'tpaPopup':
                f = i
        print(f.get_attribute('id'))
        driver.switch_to.frame(f)
        print('switch frame')
        driver.find_element(By.ID, "lastName-field").click()
        driver.find_element(By.ID, "lastName-field").send_keys('Edited')

        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Update Address")]').click()

    @classmethod  # важно
    def tearDown(self):
        self.driver.quit()


class ChromeDeleteAddresses(unittest.TestCase):
    @classmethod  # важно
    def authorize(cls, account):  # Варианты авторизации ['Facebook','Google','Email']
        driver = cls.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        sleep(3)
        type_login = ['Facebook', 'Google', 'Email']
        if account == 'Email':
            driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
            driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
            driver.implicitly_wait(5)
        elif account == 'Google':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="ggl-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(h.google_email)
            driver.find_element(By.XPATH, '//div[@id="identifierNext"]').click()
            sleep(2)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(h.google_pasw)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//div[@id="passwordNext"]').click()
            driver.switch_to.window(driver.window_handles[0])
        elif account == 'Facebook':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="fb-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(h.fb_email)
            driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(h.fb_pass)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@name="login"]').click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod  # важно
    def setUpClass(cls):
        #KillProcess.killproc('chromedriver.exe')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://qasvus.wixsite.com/ca-marketing")
        sleep(5)
        cls.authorize('Email')  # Варианты авторизации ['Facebook','Google','Email']
        sleep(5)

    def test_delete_address(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing/account/my-addresses")
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        print('press menu')
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"My Addresses")]').click()
        print('press my_address')
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="My Addresses"]'))
        print('switch iframe_MyAddress')
        sleep(3)
        driver.find_element(By.XPATH, '//div[@id="root"]/div/main/section/div/ul/li/div/div/div/button').click()
        print('click delete')
        driver.find_element(By.XPATH,
                            '//div[@id="root"]/div/main/section/div/ul/li/div/div/div/span/div/button').click()
        print('confirm delete')

    @classmethod  # важно
    def tearDown(self):
        self.driver.quit()


class ChromeSetDefaultAddresses(unittest.TestCase):
    @classmethod  # важно
    def authorize(cls, account):  # Варианты авторизации ['Facebook','Google','Email']

        driver = cls.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        sleep(3)
        type_login = ['Facebook', 'Google', 'Email']
        if account == 'Email':
            driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
            driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
            driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
            driver.implicitly_wait(5)
        elif account == 'Google':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="ggl-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(h.google_email)
            driver.find_element(By.XPATH, '//div[@id="identifierNext"]').click()
            sleep(2)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(h.google_pasw)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//div[@id="passwordNext"]').click()
            driver.switch_to.window(driver.window_handles[0])
        elif account == 'Facebook':
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
            driver.find_element(By.XPATH, '//button[@id="fb-login"]').click()
            driver.implicitly_wait(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(h.fb_email)
            driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(h.fb_pass)
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//input[@name="login"]').click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            driver.switch_to.window(driver.window_handles[0])

    @classmethod  # важно
    def setUpClass(cls):
        #KillProcess.killproc('chromedriver.exe')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://qasvus.wixsite.com/ca-marketing")
        sleep(5)
        cls.authorize('Email')  # Варианты авторизации ['Facebook','Google','Email']
        sleep(5)

    def test_make_default_address(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing/account/my-addresses")
        driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
        print('press menu')
        sleep(2)
        driver.find_element(By.XPATH, '//div[contains(text(),"My Addresses")]').click()
        print('press my_address')
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="My Addresses"]'))
        print('switch iframe_MyAddress')
        sleep(3)
        print(driver.find_element(By.XPATH, '//div[@id="root"]/div/main/section/div/ul/li/div/div/div[2]/button').text)
        driver.find_element(By.XPATH, '//div[@id="root"]/div/main/section/div/ul/li/div/div/div[2]/button').click()
        # driver.find_element(By.XPATH, '//button[contains(text(),"Make this")]').click()
        print('click default')

    @classmethod  # важно
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
       testRunner=HtmlTestRunner.HTMLTestRunner(output='d:/Documents/GitHub/Selenium/FinalProject''/HtmlReports'))

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output='d:/Documents/GitHub/Selenium/ReportsH''/HtmlReports'))
#
