import time

from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

service = SafariService()
driver = webdriver.Safari(service=service)

expected_url_1 = "https://vm619644.eurodir.ru/"
expected_title = "Главная страница"
# expected_source =

driver.get(expected_url_1)

current_url = driver.current_url
current_title = driver.title
current_source = driver.page_source

# print(current_source)

time.sleep(2)
# print(current_title)
# print(f"Expected url - {expected_url}")
# print(f"Current url - {url}")
assert expected_url_1 == current_url, "Wrong url"
assert expected_title == current_title, "Wrong title"
# assert expected_source == current_source, "Wrong html code of page"