import unittest
from time import sleep
import random
import HtmlTestRunner
from WixTest import helper as h
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyautogui as root


from KillProcess import killproc

# killproc('chromedriver.exe')

# @unittest.skip
class ChromeAuthorization(unittest.TestCase):

    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)
        sleep(5)

    def setUp(self):
        driver = self.driver
        try:
            driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
            sleep(2)
            driver.find_element(By.XPATH, '//div[contains(text(),"Log Out")]').click()
            sleep(5)
        except:
            pass

    # @unittest.skip
    def test_Google_auth(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        sleep(2)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        driver.implicitly_wait(5)
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


    # @unittest.skip
    def test_Facebook_auth(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        sleep(2)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        driver.implicitly_wait(5)
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

    # @unittest.skip
    def test_Email_auth(self):
        driver = self.driver
        sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
        driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
        driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
        driver.implicitly_wait(5)
        print('email_auth')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# @unittest.skip
class ChromeMainMenu(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)

    # @unittest.skip
    def test_1Home(self):
        driver = self.driver
        p = driver.find_element_by_xpath("//*[text()='Home']")
        sleep(2)
        assert driver.title == 'Home | California Marketing'

    # @unittest.skip
    def test_2Blog(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_partial_link_text("Blog").click()
        sleep(2)
        driver.implicitly_wait(5)
        assert driver.title == 'Blog | California Marketing'

    @unittest.expectedFailure
    def test_Shop(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Shop").click()
        sleep(2)
        assert driver.title == 'Shop | California Marketing'

    # @unittest.skip
    def test_3Services(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Services").click()
        sleep(2)
        assert driver.title == 'Services | California Marketing'

    def test_4Plans(self):    # Решение через одно место, кнопка не нажимается
        driver = self.driver
        p = driver.find_element_by_xpath("//a[contains(@href,'plans-pricing')]")
        # print(p.get_attribute('href'))
        driver.get(p.get_attribute('href'))
        sleep(2)
        assert driver.title == 'Plans & Pricing | California Marketing'
        sleep(2)
        # assert driver.title == 'News'

    @unittest.expectedFailure
    def test_News(self):    # Решение через одно место, кнопка не нажимается
        driver = self.driver
        p = driver.find_element_by_xpath("//a[contains(@href,'News')]")
        driver.get(p.get_attribute('href'))
        sleep(2)
        assert driver.title == 'News | California Marketing'
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# @unittest.skip
class ChromeSocialBtns(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)

    @unittest.expectedFailure
    def test_facebook_btn(self): #по два раза
        driver = self.driver
        btn_arr = driver.find_elements_by_xpath("//a[contains(@href,'facebook')]")
        # for x in btn_arr:
        driver.get(btn_arr[0].get_attribute('href'))
        sleep(2)
        driver.implicitly_wait(5)
        #auth_facebook
        driver.find_element(By.XPATH, "//input[@data-testid='royal_email']").send_keys(h.fb_email)
        driver.find_element(By.XPATH, "//input[@data-testid='royal_pass']").send_keys(h.fb_pass)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@data-testid='royal_login_button']").click()
        driver.implicitly_wait(5)
        sleep(3)

        driver.back()
        sleep(1)
        # self.assertIn('Silicon',driver.title)
        driver.back()
        sleep(1)
        driver.back()

    def test_twitter(self):
        driver = self.driver
        btn_arr = driver.find_elements_by_xpath("//a[contains(@href,'twitter')]")
        # print(len(btn_arr))
        # for x in btn_arr:   #работает только один раз
        #     print(x,x.get_attribute('href'))
        driver.get(btn_arr[0].get_attribute('href'))
        sleep(2)
        #auth_twitter
        driver.implicitly_wait(5)
        sleep(2)
        self.assertIn('Silicon',driver.title)
        driver.back()
        sleep(4)

    def test_VK(self):
        driver = self.driver
        btn_arr = driver.find_elements_by_xpath("//a[contains(@href,'vk.com')]")
        driver.get(btn_arr[0].get_attribute('href'))
        #auth_vk
        driver.implicitly_wait(5)
        sleep(2)
        self.assertIn('Silicon',driver.title)
        driver.back()
        sleep(1)

    def test_youtube(self):
        driver = self.driver
        btn_arr = driver.find_elements_by_xpath("//a[contains(@href,'youtube')]")
        driver.get(btn_arr[0].get_attribute('href'))
        driver.implicitly_wait(5)
        sleep(2)
        self.assertIn('Efremov',driver.title)
        driver.back()
        sleep(1)

    def test_random_link(self):
        driver = self.driver
        btn_arr = driver.find_elements_by_xpath("//a[contains(@href,'cnn.com')]")
        driver.get(btn_arr[0].get_attribute('href'))
        driver.implicitly_wait(5)
        sleep(2)
        self.assertIn('CNN',driver.title)
        driver.back()
        sleep(1)

    def test_linkedIn(self):
        driver = self.driver
        btn_arr = driver.find_elements_by_xpath("//a[contains(@href,'linkedin')]")
        driver.get(btn_arr[0].get_attribute('href'))
        driver.implicitly_wait(5)
        sleep(2)
        self.assertIn('Silicon',driver.title)
        driver.back()
        sleep(1)

    def test_GetInTouch(self):
        driver = self.driver
        btn_arr = driver.find_element_by_xpath("//a[contains(@href,'weather')]")
        driver.get(btn_arr.get_attribute('href'))
        driver.implicitly_wait(5)
        sleep(2)
        self.assertIn('Weather', driver.title)
        driver.back()
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# Чтобы не спамили тестами.
# @unittest.skip
class ChromeChat(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.test_page)
        # cls.driver.get(h.home_page)

    def test_chat(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Wix Chat']"))
        driver.find_element_by_xpath('//button[@data-hook="expand-button"]').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//textarea[@role='textbox']").send_keys('blabla-bla')
        sleep(3)
        driver.find_element_by_xpath('//button[@data-hook="emoji-keyboard"]').click() ## хз, но надо 2! раза посылать click
        driver.find_element_by_xpath('//button[@data-hook="emoji-keyboard"]').click()
        sleep(3)
        arr = driver.find_elements_by_xpath('//button[@data-hook="emoji"]')
        arr[0].click()
        # for i in range(5):
        #     arr[random.randint(0,len(arr))].click()
        #     driver.implicitly_wait(2)
        driver.find_element_by_xpath('//button[@data-hook="send-button"]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class ChromeLabelsTest(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)

    def test_labels_CALIFORNIA_MARKETING(self):
        driver = self.driver
        driver.implicitly_wait(5)
        a = driver.find_element_by_partial_link_text("CALIFORNIA MARKETING")
        self.assertEqual(a.get_attribute('href'), 'https://qasvus.wixsite.com/ca-marketing')

    def test_labelsCreativeAgency(self):
        driver = self.driver
        driver.implicitly_wait(5)
        a = driver.find_element_by_partial_link_text("A Full-Stack Creative Agency")
        self.assertEqual(a.get_attribute('href'), 'https://www.typingclub.com/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class ChromeTypingBot(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)

    def test_Bot(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_partial_link_text("A Full-Stack Creative Agency").click()
        sleep(3)
        main_window = driver.window_handles[0]
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.find_element_by_partial_link_text("Get Started").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//a[@tabindex='98']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@tabindex='100']").click()
        driver.implicitly_wait(5)

        for m in range(3): #Хватит и 3-х тестов, их там 15 примерно
            a = driver.find_elements_by_xpath("//span[@class='token_unit  _clr']")
            str = ''
            for i in a:
                str +=i.text
            actions = ActionChains(driver)
            actions.send_keys(str)
            actions.perform()
            # print(str)

        driver.get('https://www.typingclub.com/sportal/program-3/3242.play')
        sleep(2)
        for m in range(4):
            a = driver.find_elements_by_xpath("//span[@class='token_unit  _clr']")
            # print(m, len(a))
            str = ''
            for i in a:
                str += i.text
            # print(str)
            actions = ActionChains(driver)
            actions.send_keys(str)
            actions.perform()
            sleep(1)

        driver.close()
        driver.switch_to.window(main_window)
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class ChromeShoping(unittest.TestCase):

    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)


    # @unittest.skip
    def test_1buyFirstItem(self):
        driver = self.driver
        sleep(5)
        driver.find_element_by_partial_link_text("Prodact 1").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//li[1]//label[1]//input[1]').send_keys('\n')
        sleep(2)
        driver.find_element_by_xpath("//span[@class='_11lkb']").click()
        sleep(5)
        driver.find_element_by_xpath("//button[contains(@class,'addToCartButton')]").send_keys('\n')
        sleep(5)

    # @unittest.skip
    def test_2buySecondItem(self):
        driver = self.driver
        driver.get(h.home_page)
        driver.implicitly_wait(5)
        sleep(3)
        driver.find_element_by_partial_link_text("I'm a product 2").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//span[@class='_11lkb']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[contains(@class,'addToCartButton')]").send_keys('\n')

    # @unittest.skip
    def test_checkBasket(self):
        driver = self.driver
        driver.get(h.home_page+'/cart')
        driver.implicitly_wait(15)
        e = driver.find_element_by_xpath('//iframe[@title="Cart Page"]')
        # print(e)
        driver.switch_to.frame(e)
        sleep(2)
        print(driver.find_element_by_xpath('//dd[@id="total-sum"]').text)
        driver.find_element_by_xpath('//button[@data-hook="checkout-button-button"]').click()
        driver.implicitly_wait(5)
        driver.switch_to.default_content()
        seq = driver.find_elements_by_tag_name('iframe')
        # Для теста , найти по индексу, по другому заколебался
        # print(seq)
        # for x in seq:
        #     print(x.get_attribute('id'), x.get_attribute('name'))
        driver.switch_to.frame(seq[3])
        sleep(2)
        driver.find_element_by_xpath('//button[@data-hook="error-action"]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class ChromeMisic(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)

    def test_music(self):
        driver = self.driver
        driver.switch_to.default_content()
        seq = driver.find_elements_by_tag_name('iframe')
        # Для теста , найти по индексу, по другому заколебался
        # print(seq)
        # for x in seq:
        #     driver.switch_to.default_content()
        #     # print(x.get_attribute('id'), x.get_attribute('name'), x.get_attribute('title'))
        #     driver.switch_to.frame(x)
        driver.switch_to.frame(seq[-1])

        sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@title="Wix Music"]'))
        sleep(2)
        # print(driver.find_element_by_xpath("//button[@aria-label='Play']").text)
        driver.find_element_by_xpath("//button[@aria-label='Play']").click()
        # print(driver.find_element_by_xpath("//button[@aria-label='Play']").text)
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class ChromeVideo(unittest.TestCase):
    @classmethod  # важно
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(h.home_page)

    def test_video(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        # driver.implicitly_wait(10)
        sleep(10)
        driver.find_element_by_link_text('Watch Now').click()
        sleep(3)
        root.screenshot(region=(0, 0, 600, 1000), imageFilename='screen.png')
        root.moveTo(500, 940)
        root.click()
        sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()