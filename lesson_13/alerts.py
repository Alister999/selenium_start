import inspect
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")

# мы можем добавить в аргументы хром драйвер менеджер это driver_version="114.0.5735.90"
# для работы с конкретной версией драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/alerts/") #https://hh.ru/")

CALL_ALERT_BTN = ("xpath", "//button[@id='alertButton']")
CALL_TWICE_ALERT_BTN = ("xpath", "//button[@id='confirmButton']")
CALL_PROMT_ALERT_BTN = ("xpath", "//button[@id='promtButton']")

# call_alert_btn = wait.until(EC.element_to_be_clickable(CALL_ALERT_BTN))
# call_alert_btn.click()
# call_twice_alert_btn = wait.until(EC.element_to_be_clickable(CALL_TWICE_ALERT_BTN))
# call_twice_alert_btn.click()
call_promt_alert_btn = wait.until(EC.element_to_be_clickable(CALL_PROMT_ALERT_BTN))
call_promt_alert_btn.click()

time.sleep(1)

# находим алерт через явное ожидание
alert = wait.until(EC.alert_is_present())
# переключаем работу драйвера со страницы на алерт
driver.switch_to.alert
# получить текст алерта
# print(alert.text)
# принимаем алерт
# alert.accept()
# если есть алерт с ок и кенсел - можем прожать еще дисмисс
# alert.dismiss()
# для алертов с вводом текста можем его вводить как в обычное поле и принимать
alert.send_keys("Hi!")
alert.accept()

time.sleep(3)