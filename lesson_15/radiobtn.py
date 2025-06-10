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



expected_url = "https://demoqa.com/radio-button" #"https://demoqa.com/checkbox" #"https://saby.ru/"
driver.get(expected_url)

RADIO_BTN_STATUS = ("xpath", '//input[@id="yesRadio"]')
RADIO_BTN_ACTION = ("xpath", '//label[@for="yesRadio"]')
NO_RADIO_BTN_STATUS = ("xpath", '//input[@id="noRadio"]')

print(driver.find_element(*RADIO_BTN_STATUS).is_enabled())
print(driver.find_element(*RADIO_BTN_STATUS).is_selected())
wait.until(EC.element_to_be_clickable(RADIO_BTN_ACTION)).click()
print(driver.find_element(*RADIO_BTN_STATUS).is_selected())

print(driver.find_element(*NO_RADIO_BTN_STATUS).is_enabled())

sleep(3)
