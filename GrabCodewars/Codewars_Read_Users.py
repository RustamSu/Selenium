import json
from time import sleep

from selenium import webdriver
from GrabCodewars import helper as h

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.codewars.com/users/{}/{}".format(h.user,h.group[1])
driver.get(url)

sleep(1)

l = 0
len(driver.find_elements_by_xpath('//table'))
while True:
    if len(driver.find_elements_by_xpath('//table')) == l: break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    l += 1

a = []
arr = driver.find_elements_by_xpath('//tr')
for x in arr:
    a.append(x.get_attribute('data-username'))

print(a)
with open('users.json', 'w') as json_file:
    json.dump(a, json_file, indent=4)
driver.close()
