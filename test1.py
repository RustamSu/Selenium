from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#KillProcess.killproc('chromedriver.exe')

# fp = webdriver.FirefoxProfile()
# fp.set_preference("browser.link.open_newwindow",3)
#fp.set_preference("browser.link.open_newwindow.restriction", 2)
#driver = webdriver.Firefox(firefox_profile=fp)

driver = webdriver.Firefox()
driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")
# driver.maximize_window()
sleep(2)
driver.implicitly_wait(3)
driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='fb-like fb_iframe_widget']//iframe"))
#
print(driver.find_element(By.XPATH, "//button[@title='Like']").tag_name)
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//button[@title='Like']").click()
# driver.switch_to.window(driver.window_handles[1])
sleep(5)

# driver.switch_to.window(driver.window_handles[0])


# soc_net = ['twitter', 'linkedin', 'google-plus']
# xp = "//a[@data-button-type='"+soc_net[1]+"']"
#print(xp)
# element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xp)))
# element.location_once_scrolled_into_view
# element.click()
# sleep(3)
# Window_List = driver.window_handles
# driver.switch_to.window(Window_List[-1])
#driver.switch_to.window(driver.window_handles[1])
#driver.switch_to.window(driver.window_handles[1])
#driver.close()
#driver.switch_to.window(driver.window_handles[0])
#driver.find_element(By.XPATH, xp).click()
# for s in soc_net:
#     element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-button-type='" + s + "']")))
#     element.location_once_scrolled_into_view
#     element.click()
#     sleep(3)
#     print(s, driver.window_handles)
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])

# driver.find_element(By.XPATH,"//a[@data-button-type='linkedin']").click()
# driver.find_element(By.XPATH,"//a[@data-button-type='google-plus']").click()


driver.close()

