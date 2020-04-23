import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Kroger import helper as h


class ChromeMenuAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        sleep(2)

    def test_authorization(self):
        driver = self.driver
        driver.get('http://kroger.com')
        sleep(2)
        driver.find_element_by_xpath("//img[@class='Image']").click()
        actions = ActionChains(driver)
        sleep(2)
        menu = driver.find_element_by_xpath('//li[@id="WelcomeDesktop-welcome"]/div')
        actions.move_to_element(menu).perform()
        hidden_submenu = driver.find_element_by_xpath('//li[@id="WelcomeDesktop-welcome"]/div/ul/li[7]/a')
        hidden_submenu.click()
        driver.get('http://kroger.com/signin')
        driver.find_element_by_xpath("//input[@id='SignIn-emailInput']").send_keys(h.email)
        driver.find_element_by_xpath("//input[@id='SignIn-passwordInput']").send_keys(h.email_pass)
        driver.find_element_by_xpath("//button[@id='SignIn-submitButton']").click()

        # driver.implicitly_wait(15)  ## важно время, иногда работает с 5 сек.
        sleep(15)
        name = driver.find_element_by_xpath("//li[@id='WelcomeDesktop-welcome']/div/button/div/div").text
        if name != 'Sign In':
            print('Authorization OK!')
        else:
            print('Authorization NO-o-o ((((')

    def test_mainMenu(self):
        # Test links by get
        driver = self.driver
        driver.get('http://kroger.com')
        sleep(2)
        driver.find_element_by_xpath("//button[@class='bg-default-50 p-0']//*[local-name()='svg']").click()
        Mmenu = driver.find_elements(By.XPATH, "//div[@class='SiteMenu-ListContent']//div/div/a")
        ListMmenu = []
        for n in Mmenu:
            ListMmenu.append((n.text, n.get_attribute('href')))

        for n in ListMmenu:
            driver.get(n[1])
            print(driver.title)

    def test_SubMenu(self):
        # write submenus into the json
        driver = self.driver
        driver.get('http://kroger.com')
        sleep(2)
        driver.find_element_by_xpath("//button[@class='bg-default-50 p-0']//*[local-name()='svg']").click()
        MenuList = []
        SubMenu = driver.find_elements(By.XPATH, "//div[@class='SiteMenu-ListContent']//div/div/button")
        a = len(SubMenu)

        for i in range(0, a):
            SubMenu = driver.find_elements(By.XPATH, "//div[@class='SiteMenu-ListContent']//div/div/button")
            name = SubMenu[i].text
            SubMenu[i].click()
            current_menu = driver.find_elements(By.XPATH, "//div[@class='SubSiteMenu-SubList pt-8']/a")
            ListSubMenu = []
            ListItem = {}
            for k in current_menu:
                item = ''
                item = item + ('{"nameItem": "' + k.text + '",')
                item = item + ('"href": "' + k.get_attribute('href') + '"}')
                # item = item + ('"Result": "' + 'OK' + '"}')
                ListSubMenu.append(item)

            ListItem[name] = {'items': ListSubMenu}
            MenuList.append(ListItem)
            driver.find_element_by_xpath("//button[@class='kds-Button kds-Button--primaryInverse']").click()

        MenuList = str(MenuList).replace("'{", "{").replace("}'", "}").replace("'", '"')
        # print(MenuList)
        with open('output_test.json', 'w') as json_file:
            json_file.write(MenuList)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    ChromeMenuAuth.main()
