import os
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# Специфические настройки меняющие пути и параметры
# сейчас передаем путь для загрузки
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads",

}
# через этот метод добавляем опции, которые не доступны из коробки
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options   )

expected_url = "https://saby.ru/"

driver.get(expected_url)
help_btn = driver.find_element("xpath", "//a[text()='Поддержка']")
help_btn.click()

time.sleep(1)

download_btn = driver.find_element("xpath", "//h5[text()='Скачать']")
download_btn.click()

time.sleep(1)

#при этом файл скачивается в дефолтную директорию
download_file = driver.find_element("xpath", "//a[text()='Скачать (Exe 10.40 МБ) ']")
download_file.click()


time.sleep(3)