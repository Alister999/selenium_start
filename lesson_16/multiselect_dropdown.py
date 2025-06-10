import os
from time import sleep

from  selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

# options = Options()
# options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) #, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)



expected_url = "https://demoqa.com/select-menu" #"https://demoqa.com/checkbox" #"https://saby.ru/"
driver.get(expected_url)

# современные селекты сделаны через дивы, и в глубине есть инпут
# SELECT_INPUT = ("xpath", '//input[@id="react-select-3-input"]')
#
# # находим инпут
# input_field = driver.find_element(*SELECT_INPUT)
# # вводим совпадающие данные
# input_field.send_keys("Dr.")
# # выбираем найденное энтером
# input_field.send_keys(Keys.ENTER)

# еще способ - инспектировать опции через остановку js
# вводим этот код в консоли - setTimeout(function() {debugger; }, 5000);
# открываем нужный нам селект
# и это приостанавливает на 5 секунд выполнение js на странице
# и далее спокойно находим локатор элемента
# SELECT_DIV = ("xpath", '//div[text()="Select Title"]')
# FIRST_OPTION = ("xpath", '//div[@id="react-select-3-option-0-0"]')
#
# wait.until(EC.element_to_be_clickable(SELECT_DIV)).click()
# wait.until(EC.element_to_be_clickable(FIRST_OPTION)).click()

# и мультиселект
SELECT_INP = ("xpath", '//input[@id="react-select-4-input"]')

wait.until(EC.element_to_be_clickable(SELECT_INP)).send_keys("Green")
driver.find_element(*SELECT_INP).send_keys(Keys.ENTER)
wait.until(EC.element_to_be_clickable(SELECT_INP)).send_keys("Bla")
# или через таб автодополнить неполный ввод и выбрать
driver.find_element(*SELECT_INP).send_keys(Keys.TAB)

sleep(2)


# это все для старых селектов
# SELECT_FIELD = ("xpath", '//select[@id="oldSelectMenu"]')
# OPTIONS = ("xpath", '//select[@id="oldSelectMenu"/option[@value="1"]]')
#
# # получаем объект селекта
# SELECT_OBJ = Select(driver.find_element(*SELECT_FIELD))
# # получаем все опции этого селекта
# all_options = SELECT_OBJ.options

# for opt in all_options:
#     # option_txt = opt.text
#     SELECT_OBJ.select_by_index(all_options.index(opt))
    # print(option_txt)
    # if "White" == option_txt:
    #     print("--__Option exist__--")
    # SELECT_OBJ.select_by_visible_text(option_txt)
# print(all_options)

# можно выбирать по тексту опции
# SELECT_OBJ.select_by_visible_text("Blue")
# или по велью
# SELECT_OBJ.select_by_value("1")
# или по индексу
# SELECT_OBJ.select_by_index(1)



# wait.until(EC.element_to_be_clickable(SELECT_FIELD)).click()
# wait.until(EC.element_to_be_clickable(OPTIONS)).click()

# sleep(2)