from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()
print(driver.find_element(By.XPATH, "//p[@class='site-title']//a[contains(text(),'California Real Estate')]")
      .get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
assert "California Real" in driver.title
print(driver.title)
driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]")
driver.find_element(By.NAME, "g2-name").send_keys("Aleksandr")
driver.find_element(By.ID, "g2-email").send_keys("9492393781p@gmail.com")
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Hello!")
driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "go back").send_keys('\n')
print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
driver.close()