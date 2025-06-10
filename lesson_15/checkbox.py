import os
from time import sleep

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

# options = Options()
# options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) #, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)



expected_url = "https://demoqa.com/selectable" #"https://demoqa.com/checkbox" #"https://saby.ru/"
driver.get(expected_url)

CHECKBOX_ACTION = ("xpath", '//label[@for="tree-node-home"]')
CHECKBOX_STATUS = ("xpath", '//input[@id="tree-node-home"]')
UNROLL_BTN = ("xpath", '//button[@aria-label="Toggle"]')

FIRST_ELEM_LIST = ("xpath", "//li[text()='Cras justo odio']")

# attrs = [attr for attr in driver.find_element(*FIRST_ELEM_LIST).get_attribute("class").split()]
# print("active" in attrs)
attrs = driver.find_element(*FIRST_ELEM_LIST).get_attribute("class")
# print(False if attrs.find("active") < 0 else True)
print("active" in attrs)

wait.until(EC.element_to_be_clickable(FIRST_ELEM_LIST)).click()

# attrs = [attr for attr in driver.find_element(*FIRST_ELEM_LIST).get_attribute("class").split()]
# print("active" in attrs)
attrs = driver.find_element(*FIRST_ELEM_LIST).get_attribute("class")
# print(False if attrs.find("active") < 0 else True)
print("active" in attrs)

# sleep(3)
# driver.find_elements(*CHECKBOX)[0].click()

# wait.until(EC.element_to_be_clickable(UNROLL_BTN)).click()
# # Если это инпут, то можно вот так получить чек или нет
# # print(driver.find_element(*CHECKBOX).get_attribute("checked"))
# # встроенный способ селениума, проверять обязательно у инпута
# print(driver.find_element(*CHECKBOX_STATUS).is_selected())
# wait.until(EC.element_to_be_clickable(CHECKBOX_ACTION)).click()
# # driver.find_element(*CHECKBOX_1).click()
# # print(driver.find_element(*CHECKBOX).get_attribute("checked"))
# print(driver.find_element(*CHECKBOX_STATUS).is_selected())


sleep(3)