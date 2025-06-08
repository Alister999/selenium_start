import inspect
import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# создаем объект опций
chrome_options = webdriver.ChromeOptions()
# стратегии загрузки страниц - нормал, игер и нан
# нан - бесполезная по сути, ничего не загружается просто браузер мигает
# нормал - дефолтная - дожидаемся загрузки всех скриптов, шрифтов, картинок
# игер - дожидается только загрузка дом - хтмл без картинок и скриптов
# chrome_options.page_load_strategy = "normal" #не надо прописывать, и так дефолтная
chrome_options.page_load_strategy = "eager"


# добавляем опцию хедлесс - запуск браузера без интерфейса в фоне, должно быть до инита драйвера
# chrome_options.add_argument("--headless")
# запуск браузера в режиме инкогнито - не используем кэш и не сохраняем данные
# chrome_options.add_argument("--incognito")
# позволяет обходить ошибки сертификата на сайте
chrome_options.add_argument("--ignore-certificate-errors")
# опция похожа на инкогнито, но без доп режима вырубает кэширование
chrome_options.add_argument("--disable-cache")
# для задания размера окна открываемого браузера
# chrome_options.add_argument("--window-size=700,700")
service = Service(executable_path=ChromeDriverManager().install())
#Добавляем опшенс как аргумент в драйвер
driver = webdriver.Chrome(service=service, options=chrome_options)
# или можно задавать размер не аргументом а методом драйвера, но будет моргание
# driver.set_window_size(700, 700)
# эта опция максимизирует окно на весь экран
# driver.maximize_window()
expected_url = "https://saby.ru/"

driver.get(expected_url)