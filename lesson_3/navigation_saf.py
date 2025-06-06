import time

from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

# Можно указать сервис, но это не обязательно
service = SafariService()  # SafariDriver встроен, путь указывать не нужно
driver = webdriver.Safari(service=service)

driver.get("https://vm619644.eurodir.ru")
time.sleep(2)

driver.get("https://vm619644.eurodir.ru/about")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)