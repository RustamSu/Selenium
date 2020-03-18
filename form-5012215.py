# http://www.123formbuilder.com/form-5012215/online-order-form
import psutil
from selenium import webdriver
import random
from selenium.webdriver.common.by import By

## to clear the memory from the chromedriver.exe
for proc in psutil.process_iter():
    if proc.name() == 'chromedriver.exe':
        proc.kill()

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")

driver.find_element_by_xpath("//input[@placeholder='First']").send_keys('Aleksandr')
driver.find_element_by_xpath("//input[@placeholder='Last']").send_keys('Kuzhelev')
driver.find_element_by_xpath("//input[@type='email']").send_keys('qqqq@gmail.com')
driver.find_element_by_xpath("//input[@placeholder='### ### #### ']").send_keys('1234567890')
driver.find_element_by_id("0000000e_" + str(random.randint(0, 5))).click()
driver.find_element_by_xpath("//input[@type='number']").send_keys(str(random.randint(1, 100)))
driver.find_element_by_id('date-00000012-month').send_keys('3')






#driver.close()

