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


expected_url = "https://saby.ru/" #"https://demoqa.com/checkbox" #"https://saby.ru/"
driver.get(expected_url)

# print(driver.current_window_handle)
# print(driver.window_handles)

start_job_btn = driver.find_element("xpath", '//button[@id="header-menu-btn"]')
start_job_btn.click()

sleep(2)

# эта команда открывает новую вкладку/окно в зависимости от переданного аргумента
# прикол этого метода в том, что драйвер автоматом переключается на новую вкладку/окно
driver.switch_to.new_window("tab")
# окно
driver.switch_to.new_window("window")
driver.get("https://ya.ru")
# для закрытия окна
driver.close()

# ВНИМАНИЕ! ДЛЯ РАЗДЕЛЕНИЯ СЕССИЙ(НАПРИМЕР ДЛЯ ДВУХ ЮЗЕРОВ) НУЖНО СОЗДАТЬ НОВЫЙ ДРАЙВЕР!

# переключение на актуальное окно
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])

# работа с окнами происходит через дескрипторы
# так мы получаем дескриптор текущего окна
# print(driver.current_window_handle)
# а так получаем дескрипторы всех окон
# print(driver.window_handles)
# теперь делаем переменную со всеми десркипторами вкладок
# tabs = driver.window_handles
# # и переключаемя на следующее окно
# driver.switch_to.window(tabs[1])
#
# expected_login = os.getenv("LOGIN")
# expected_password = os.getenv("PASS")
#
#
# login_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-10" and @type="text"]')
# passw_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-10" and @type="password"]')
# send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
#
# login_field.send_keys(expected_login)
# send_btn.click()
# sleep(1)
#
# passw_field.send_keys(expected_password)
# send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
# send_btn.click()





# # send_btn.click()
#
#
# # tarif_btn = driver.find_element("xpath", "//a[@href='/tariffs']")
# #
# # tarif_btn.click()
# #
sleep(5)