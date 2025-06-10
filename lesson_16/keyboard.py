import os
from time import sleep

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from selenium.webdriver import Keys

# options = Options()
# options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) #, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)


expected_url = "https://the-internet.herokuapp.com/key_presses" #"https://demoqa.com/checkbox" #"https://saby.ru/"
driver.get(expected_url)

INPUT_FIELD = ("xpath", '//input[@id="target"]')

input_field = wait.until(EC.element_to_be_clickable(INPUT_FIELD))
# так с помощью класса кейс мы можем эмулировать нажатия клавиш с клавиатуры
# input_field.send_keys(Keys.ENTER)
# сочетания клавиш
# input_field.send_keys(Keys.SHIFT + "a")
# хотим выделить весь ввдеденный текст
input_field.send_keys("asdfasdfasdfa")
sleep(1)
input_field.send_keys(Keys.COMMAND + "A")
sleep(1)
input_field.send_keys(Keys.BACKSPACE)
# input_field.send_keys("qwertyuiop[]\\asdfghjkl;'zxcvbnm,./")

sleep(3)