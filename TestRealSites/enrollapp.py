# https://enrollapp.com/
# Starts tests
import random
import time
from selenium import webdriver
import KillProcess

# if only Yes and No
def TestYesNo():
    try:
        return driver.find_element_by_xpath("//div[contains(@class,'button-group-stack-small')]").is_enabled()
    except:
        return False

def TestRadio():
    try:
        return driver.find_element_by_xpath("//input[contains(@id,'choice')]").is_enabled()
    except:
        return False

my_email = 'alexkuzh@gmail.com'
passw = '$h$U*#hzf6q.XB6'
KillProcess.killproc('chromedriver.exe') #kill chromedriver.exe #можно вставить для очистки памяти
driver = webdriver.Chrome()
driver.get("https://enrollapp.com")
driver.maximize_window()

# authorisation
driver.find_element_by_xpath("//a[contains(text(),'Sign In')]").click()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@id='user_email']").send_keys(my_email)
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@id='user_password']").send_keys(passw)
time.sleep(1)

driver.find_element_by_xpath("//input[@name='commit']").click()
time.sleep(2)

#for i in range(7):
while int(driver.find_element_by_xpath("//strong[contains(text(),'answered')]").text[:4]) <= 3000: #limit
    print(driver.find_element_by_xpath("//strong[contains(text(),'answered')]").text[:4])
    try:
        driver.find_element_by_xpath("//a[@class='button']").click()
    except:
        pass
    if TestYesNo():
        xp = "//div[contains(@class,'button-group')]/button[@class='button']["+str(random.randint(1, 2))+"]"
        driver.find_element_by_xpath(xp).click()
        driver.find_element_by_xpath("//button[@class='button']").click()
        print('Yes_NO')
    elif TestRadio():
        r = len(driver.find_elements_by_xpath("//input[contains(@id,'choice')]"))
        xp = "//ul[contains(@class,'vertical-checklist')]/li["+str(random.randint(1, r))+"]"
        driver.find_element_by_xpath(xp).click()
        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("//button[@class='button']").click()
        print('Radio',r)
    driver.implicitly_wait(1)

print('end')
driver.close()
