import os
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

expected_url = "https://convertio.co/ru/"

driver.get(expected_url)

time.sleep(1)

# upload_btn = driver.find_element("xpath", "//span[text()='Выберите файлы']")
# upload_btn.click()
#Так как мы не можем работать в селениуме напрямую с системой, ищем инпут, тайп файл
inp_file = driver.find_element("xpath", "//input[@type='file' and @id='pc-upload-add']")
# и делаем как бы ввод с клавиатуры в данный инпут, но пути до файла
inp_file.send_keys(f"{os.getcwd()}/downloads/saby-setup-web.exe")
# если не можем поверхностно найти инпут - ищем поиском, он часто скрыт но всегда есть на странице загрузки



time.sleep(3)