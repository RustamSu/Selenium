import unittest
from time import sleep
import json
from selenium import webdriver
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Johnlewis import helper as h


class ChromeMainMenu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        sleep(1)

    def test_Menu(self):
        driver = self.driver
        driver.get("https://www.johnlewis.com")

        menu = driver.find_elements_by_xpath('//nav[@aria-label="Main menu"]//a["@href"]')
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.get_attribute('textContent')
            l = x.get_attribute('href')
            r = requests.get(l)
            d['name'] = t if t[0] != '<' else 'images'
            d['link'] = l
            d['status code'] = r.status_code
            if r.status_code != 200:
                print(t, l)
            map_menu.append(d)
        with open('output_test.json', 'w') as json_file:
            json.dump(map_menu, open('output_test.json', 'w'))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    ChromeMainMenu.main()
