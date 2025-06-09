import inspect
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# здесь мы задаем таймер ожидания поялвения элементов
# применяется к файнд элемент/с
# примерно раз в секунду идет проверка присутствия кнопки,
# как только найдена - вейт останавливается
# советуют использовать явные ожидания вместо неявных для работы с конкретным элементом
# не надо мешать явные и неявные ожидания
driver.implicitly_wait(10)

expected_url = "https://saby.ru/"

driver.get(expected_url)

START_JOB_BTN = ("xpath", '//button[@id="header-menu-btn"]')

start_job_btn = driver.find_element(*START_JOB_BTN)
start_job_btn.click()