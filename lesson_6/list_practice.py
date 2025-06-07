import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)



expected_url = "https://saby.ru/"

driver.get(expected_url)
btns = driver.find_elements("class name", "sbisru-Button")

btns[2].click()

# for elem in btns:
#     print(elem.text)

# btn.click()

time.sleep(2)