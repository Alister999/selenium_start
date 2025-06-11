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

expected_url = "https://demoqa.com/nestedframes" #"https://demoqa.com/checkbox" #"https://saby.ru/"
driver.get(expected_url)

FRAME_1 = ("xpath", '//iframe[@id="frame1"]')
FRAME_2 = ("xpath", '//iframe')
OUTSIDE_FRAME = ("xpath", '//h1[@class="text-center"]')

# если код находится в айфрейме нужно перереключиться на него
# driver.switch_to.frame("id or name or web elem or index")
# когда надо переключиться на основной контент вне айфрейма
# driver.switch_to.default_content()

# вложенные фреймы
frame_1 = driver.find_element(*FRAME_1)
#переключение на фрейм первого уровня по веб элементу
driver.switch_to.frame(frame_1)
print(driver.find_element("xpath", "//body").text)
# переключение на дочерний фрейм по индексу
driver.switch_to.frame(0)
print(driver.find_element("xpath", "//body").text)
# вернуться на фрейм назад
driver.switch_to.parent_frame()
print(driver.find_element("xpath", "//body").text)
#переключаемся на основное окно и ищем там элемент
driver.switch_to.default_content()
print(driver.find_element(*OUTSIDE_FRAME).text)
