from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from BrowserStack import helpers as h

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '80.0',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '1920x1080',
    'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor= h.command_exec,
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()