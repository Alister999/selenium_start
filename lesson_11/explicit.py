import inspect
import os
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# в явном ожидании мы указываем условия не для всех, а для конкретного элемента
# Создаем экземпляр вебдрайвер вейт
# принимает драйвер, сколько ждем, и с какой частотой опрашиваем страницу(1 это раз в секунду)
wait = WebDriverWait(driver, 15, poll_frequency=1)

expected_url = "https://saby.ru/"
driver.get(expected_url)

START_JOB_BTN = ("xpath", '//button[@id="header-menu-btn"]')

# здесь в переменную кладем запрос кнопки после ожидания когда появится,
# кортеж не надо распаковывать
# здесь ждем пока элемент не появится в дом и высота не нулевая
# start_job_btn = wait.until(EC.visibility_of_element_located(START_JOB_BTN))
#здесь ждем, пока элемент не станет кликабельным
# база, бестпрактис по кликам
start_job_btn = wait.until(EC.element_to_be_clickable(START_JOB_BTN))
start_job_btn.click()
# ждем исчезновения элемента и идем далее
# wait.until(EC.invisibility_of_element_located(START_JOB_BTN))
# print("All OK")
# здесь мы ждем пока элемент приобретет нужный нам атрибут
# здесь написано не верно, это для текстового поля
# wait.until(EC.text_to_be_present_in_element_value(START_JOB_BTN, "Начать работу"))
# print("All OK")
# time.sleep(2)

expected_login = os.getenv("LOGIN")
expected_password = os.getenv("PASS")

LOGIN_FIELD = ("xpath", '//input[@name="ws-input_2025-06-07" and @type="text"]')
PASS_FIELD = ("xpath", '//input[@name="ws-input_2025-06-07" and @type="password"]')
SEND_BTN = ("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')


# login_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-07" and @type="text"]')
# passw_field = driver.find_element("xpath", '//input[@name="ws-input_2025-06-07" and @type="password"]')
# send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
# send_btn2 = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')

# переключение на актуальное окно
windows = driver.window_handles
driver.switch_to.window(windows[-1])

login_field = wait.until(EC.element_to_be_clickable(LOGIN_FIELD))
login_field.send_keys(expected_login)
wait.until(EC.text_to_be_present_in_element_value(LOGIN_FIELD, expected_login))
send_btn = wait.until(EC.element_to_be_clickable(SEND_BTN))
send_btn.click()

wait.until(EC.element_to_be_clickable(PASS_FIELD)).send_keys(expected_password)
wait.until(EC.text_to_be_present_in_element_value(PASS_FIELD, expected_password))
wait.until(EC.element_to_be_clickable(SEND_BTN)).click()


# send_btn.click()
#
# login_field.send_keys("AAAAAAAAAAAA")
# time.sleep(1)
# login_field.clear()
# login_field.send_keys(expected_login)
# # print(f"Entry text of login field - {login_field.get_attribute("value")}")
# current_login = login_field.get_attribute("value")
# assert expected_login == current_login, "Wrong login"
# send_btn.click()
# time.sleep(1)
#
# passw_field.send_keys("BBBBBBBBBB")
# time.sleep(1)
# passw_field.clear()
# passw_field.send_keys(expected_password)
# # print(f"Entry text of password field - {passw_field.get_attribute("value")}")
# current_password = passw_field.get_attribute("value")
# assert expected_password == current_password, "Wrong password"
# send_btn = driver.find_element("xpath", '//span[@class="controls-BaseButton__wrapper controls-Button__wrapper_viewMode-filled controls-BaseButton__wrapper_captionPosition_end controls-Button_textAlign-center"]')
# send_btn.click()

# send_btn.click()


# tarif_btn = driver.find_element("xpath", "//a[@href='/tariffs']")
#
# tarif_btn.click()
#
time.sleep(5)