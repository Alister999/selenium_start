import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# Для работы через атрибуты

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

expected_url = "https://saby.ru/" #"https://vm619644.eurodir.ru/"
expected_btn_text = "Начать работу"

driver.get(expected_url)

assert expected_url == driver.current_url
assert expected_btn_text == "Начать работу"

# btn = driver.find_element(By.ID, "header-menu-btn")
# это работа через атрибуты
btn = driver.find_element("id", "header-menu-btn")
# найденный элемент - это экземпляр класса веб элемент
# print(btn.text)
# без атрибутов, через поиск по строковому значению
btn.click()

time.sleep(3)