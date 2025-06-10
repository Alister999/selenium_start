import inspect
import os
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

# options = Options()
# options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) #, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)



expected_url = "https://online.saby.ru/page/saby-app?add_gtm=true" #"https://saby.ru/"

driver.get(expected_url)

#куки до удаления
# cookies = [f"{coo['name']} == {coo['value']}" for coo in driver.get_cookies()]
#
# for c in cookies:
#     print(c)
# # удаляем все куки
# driver.delete_all_cookies()
# # записываем новую куку
# driver.add_cookie({
#     "name": "lang",
#     "value": "en"
# })
# # смотрим опять куки
# cookies = [f"{coo['name']} == {coo['value']}" for coo in driver.get_cookies()]
#
# print("After clear")
#
# for c in cookies:
#     print(c)




# также мы можем менять куки
# получаем нужную куку
# before = driver.get_cookie("lang")
# print(before)
# удаляем куку
# driver.delete_cookie("lang")
# # записываем новую куку на замену
# driver.add_cookie({
#     "name": "lang",
#     "value": "en"
# })
#
# after = driver.get_cookie("lang")
# print(after)



# а так мы можем добавлять куки
# driver.add_cookie({
#     "name": "Example",
#     "value": "hihihi!"
# })


#так мы можем получить все куки
# cookies = [f"{coo['name']} == {coo['value']}" for coo in driver.get_cookies()]
#
# for c in cookies:
#     print(c)

# а так - какую то конкретную куку по имени
# dev_id_cookie = driver.get_cookie("DeviceId")
# region_cookie = driver.get_cookie("region")
# lang_cookie = driver.get_cookie("lang")

# print(dev_id_cookie["value"])
# print(lang_cookie["value"])


# start_job_btn = driver.find_element("xpath", '//button[@id="header-menu-btn"]')
# start_job_btn.click()
#
# time.sleep(2)
#
# # переключение на актуальное окно
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])
#
# expected_login = os.getenv("LOGIN")
# expected_password = os.getenv("PASS")
#
#
# login_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-09" and @type="text"]')
# passw_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-09" and @type="password"]')
# send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
#
# login_field.send_keys(expected_login)
# send_btn.click()
# time.sleep(1)
#
# passw_field.send_keys(expected_password)
# send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
# send_btn.click()

# cookies = [f"{coo['name']} == {coo['value']}" for coo in driver.get_cookies()]
#
# for c in cookies:
#     print(c)

# чтобы сохранить куки в файл
# в аргументы передаем что сохраняем, куда и тип операции(врайт байтс)
# pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()
# также мы читаем куки из файла
cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(2)



