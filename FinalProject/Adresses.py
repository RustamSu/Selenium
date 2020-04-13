from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import KillProcess
from FinalProject import helper as h

KillProcess.killproc('chromedriver.exe')

def authorize(account):
    driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//a[@id='signUpDialogswitchDialogLink']").click()
    sleep(3)
    type_login = ['Facebook','Google','Email']
    i = account
    if type_login[i] == 'Email':
        driver.find_element(By.XPATH, "//button[@id='memberLoginDialogswitchToEmailLink']").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//input[@id="memberLoginDialogemailInputinput"]').send_keys(h.email)
        driver.find_element(By.XPATH, '//input[@id="memberLoginDialogpasswordInputinput"]').send_keys(h.passw)
        driver.find_element(By.XPATH, '//button[@id="memberLoginDialogokButton"]').click()
        driver.implicitly_wait(5)
    elif type_login[i] == 'Google':
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="memberLoginDialogsocialLoginIframe"]'))
        driver.find_element(By.XPATH, '//button[@id="ggl-login"]').click()
        driver.implicitly_wait(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(h.email)
        driver.find_element(By.XPATH, '//div[@id="identifierNext"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(h.google_pasw)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//div[@id="passwordNext"]').click()
        driver.switch_to.window(driver.window_handles[0])

    elif type_login[i] == 'Facebook':
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

def add_new_address():
    driver.find_element(By.XPATH, '//div[@id="root"]/div/main/section/div[3]/button').click() #Add new Address

    sleep(5)
    driver.switch_to.default_content()
    # fr = driver.find_elements(By.TAG_NAME,"iframe")  #это тоже работает
    # for i in fr:
    #     if i.get_attribute('id')[:8] == 'tpaPopup':
    #         f = i
    # print(f.get_attribute('id'))
    # driver.switch_to.frame(f)

    driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[contains(@id,"tpaPopup")]'))
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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qasvus.wixsite.com/ca-marketing")
sleep(5)

authorize(2)

sleep(2)

driver.get("https://qasvus.wixsite.com/ca-marketing/account/my-addresses")
driver.find_element(By.XPATH, '//button[contains(@aria-label,"Hello")]').click()
sleep(3)
driver.find_element(By.XPATH, '//div[contains(text(),"My Addresses")]').click()
sleep(3)

driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@title="My Addresses"]'))



driver.close()
