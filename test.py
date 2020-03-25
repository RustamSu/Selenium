# http://www.123formbuilder.com/form-5012215/online-order-form
import KillProcess
import unittest
from time import sleep
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

if random.randint(False, True): print(1)
# ## to clear the memory from the chromedriver.exe
# KillProcess.killproc('chromedriver.exe') #kill chromedriver.exe #можно вставить для очистки памяти
#
# driver = webdriver.Chrome()
# driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")
# driver.maximize_window()
#
# l = driver.find_elements(By.XPATH, "//label[contains(@id,'checkbox-0000000c-') and @data-role='choice']")
# l[3].click()
# sleep(10)
#
# driver.close()