import time

from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

service = SafariService()
driver = webdriver.Safari(service=service)

expected_url = "https://saby.ru/"

driver.get(expected_url)
btns = driver.find_elements("class name", "sbisru-Button")

btns[2].click()

# for elem in btns:
#     print(elem.text)

# btn.click()

time.sleep(2)