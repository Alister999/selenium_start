import inspect
import os
import time

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

expected_url ="https://hh.ru"

driver.get(expected_url)

# LOGIN_BTN = ("xpath", '//a[@data-qa="login"]')
# LOGIN_BTN_2 = ("xpath", "//span[text()='Войти']")
# MAIL = ("xpath", "//div[text()='Почта']")
# INPUT_FIELD = ("xpath", '//input[@name="username"]')
# LOGIN_BTN_3 = ("xpath", "//span[text()='Дальше']")
#
# wait.until(EC.visibility_of_element_located(LOGIN_BTN))
# wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()
# wait.until(EC.visibility_of_element_located(LOGIN_BTN_2))
# wait.until(EC.element_to_be_clickable(LOGIN_BTN_2)).click()
#
# wait.until(EC.visibility_of_element_located(MAIL))
# wait.until(EC.element_to_be_clickable(MAIL)).click()
# wait.until(EC.visibility_of_element_located(INPUT_FIELD))
# wait.until(EC.element_to_be_clickable(INPUT_FIELD)).send_keys("dr.borgaw@icloud.com")
#
#
# wait.until(EC.visibility_of_element_located(LOGIN_BTN_3))
# wait.until(EC.element_to_be_clickable(LOGIN_BTN_3)).click()
#
# time.sleep(50)
#
#
# pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies_hh.pkl", "wb"))

driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd() + "/cookies/cookies_hh.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(5)