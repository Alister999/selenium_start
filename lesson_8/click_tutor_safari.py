import inspect
import time

from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

service = SafariService()
driver = webdriver.Safari(service=service)

expected_url = "https://saby.ru/"

driver.get(expected_url)

start_job_btn = driver.find_element("xpath", '//button[@id="header-menu-btn"]')
start_job_btn.click()

time.sleep(2)

# переключение на актуальное окно
windows = driver.window_handles
driver.switch_to.window(windows[-1])

expected_login = "dr.borgaw@icloud.com"
expected_password = "Avesatan99!"


login_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-07" and @type="text"]')
passw_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-07" and @type="password"]')
send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
# send_btn2 = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')

login_field.send_keys("AAAAAAAAAAAA")
time.sleep(1)
login_field.clear()
login_field.send_keys(expected_login)
# print(f"Entry text of login field - {login_field.get_attribute("value")}")
current_login = login_field.get_attribute("value")
assert expected_login == current_login, "Wrong login"
send_btn.click()
time.sleep(1)

passw_field.send_keys("BBBBBBBBBB")
time.sleep(1)
passw_field.clear()
passw_field.send_keys(expected_password)
# print(f"Entry text of password field - {passw_field.get_attribute("value")}")
current_password = passw_field.get_attribute("value")
assert expected_password == current_password, "Wrong password"
send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
send_btn.click()

# send_btn.click()


# tarif_btn = driver.find_element("xpath", "//a[@href='/tariffs']")
#
# tarif_btn.click()
#
time.sleep(5)