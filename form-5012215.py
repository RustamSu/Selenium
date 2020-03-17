# http://www.123formbuilder.com/form-5012215/online-order-form
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")

driver.find_element_by_xpath("//input[@placeholder='First']").send_keys('Aleksandr')
driver.find_element_by_xpath("//input[@placeholder='Last']").send_keys('Kuzhelev')
driver.find_element_by_xpath("//input[@type='email']").send_keys('qqqq@gmail.com')
driver.find_element_by_xpath("//input[@placeholder='### ### #### ']").send_keys('1234567890')

