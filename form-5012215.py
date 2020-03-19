# http://www.123formbuilder.com/form-5012215/online-order-form
import KillProcess
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
from time import sleep

## to clear the memory from the chromedriver.exe
KillProcess.killproc('chromedriver.exe') #kill chromedriver.exe

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

driver.find_element_by_xpath("//input[@placeholder='First']").send_keys('Aleksandr')
driver.find_element_by_xpath("//input[@placeholder='Last']").send_keys('Kuzhelev')
driver.find_element_by_xpath("//input[@type='email']").send_keys(str(random.randrange(1000,9999))+'@gmail.com')
driver.find_element_by_xpath("//input[@placeholder='### ### #### ']").send_keys(str(random.randrange(1,9999999999)).zfill(10))

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

driver.implicitly_wait(5)
#del random choice
#driver.find_element_by_id("0000000e_" + str(random.randint(0, 5))).click() #RADIO
driver.find_element_by_id("0000000e_1").click() #RADIO

driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@type='number']").send_keys(str(random.randint(1, 100))) #quantity
driver.find_element_by_xpath("//body/form[@id='form']/div/div/div/div/div/div/div[2]").click() #Вызываем календарь
sleep(1)
driver.find_element_by_class_name("today ").click()
driver.find_element_by_xpath("//input[@placeholder='Street Address']").send_keys('Lenin street')
driver.find_element_by_xpath("//input[@placeholder='Street Address Line 2']").send_keys('Marx street')
driver.find_element_by_xpath("//input[@placeholder='City']").send_keys('Cinci')
driver.find_element_by_xpath("//input[@placeholder='Region']").send_keys('OH')
driver.find_element_by_xpath("//input[@placeholder='Postal / Zip Code']").send_keys('11111')
driver.find_element_by_xpath("//input[@placeholder='Country']").click()#send_keys('\n')
driver.implicitly_wait(5)
#driver.find_element_by_xpath("//input[@placeholder='Country']").send_keys('Albania') #самое очевидное решение для заполнения
driver.find_element_by_xpath("//*[contains(text(), 'Zambia')]").click() #можно было в input толкать, но мы же эмулируем работу пользователя, так что жмем элемент из списка

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
driver.implicitly_wait(5)

Select(driver.find_element_by_tag_name('select')).select_by_index(random.randint(0, 2)) #simple select

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
driver.implicitly_wait(5)
driver.find_element_by_tag_name('html').send_keys('\n')
#del random choice
#for i in range(3):
#    driver.find_element_by_id("00000018_"+str(random.randrange(0,2))).click()
driver.find_element_by_id("00000018_1").click()
driver.find_element_by_id("00000018_3").click()
driver.find_element_by_xpath("//input[@type='text'][@data-role='other']").send_keys('blablabla')

frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
#driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click() #Jam! # Капча нажмется, но потом разгадывание велосипедов и автобусов

# driver.find_element_by_xpath("//button[@type='submit']").click()
#driver.close()

