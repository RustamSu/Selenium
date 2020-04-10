from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.find_element(By.LINK_TEXT, "California Real Estate").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
print(driver.title)
driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

if driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]").text == 'Send Us a Message':
    driver.find_element_by_xpath("//input[@id='g2-name']").send_keys('Aleksandr Kuzhelev')
    driver.find_element_by_name("g2-email").send_keys('blabl1abla@gmail.com')
    driver.find_element_by_id("contact-form-comment-g2-message").send_keys('Hello Sergey!')
    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
    sleep(3)

    #driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()
    sleep(3)
    #driver.find_element_by_xpath("//a[contains(text(),'go back')]").send_keys('\n')
    driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()
    driver.implicitly_wait(3)

print("Button's type is", driver.find_element_by_xpath("//button[@class='pushbutton-wide']").get_attribute("type"))

driver.close()
