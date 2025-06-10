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

# данные берем при покупке либо от сюда http://free-proxy.cz/ru/ бесплатные айпи и порт
PROXY_SERVER = "213.169.33.7:4000"#"91.233.169.23:8081"
# если нам нужна авторизация на прокси то пишем с таким синтаксисом
PROXY_SERVER = "username:password@213.169.33.7:4000"

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")
# service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options) #service=service,
wait = WebDriverWait(driver, 5, poll_frequency=1)


expected_url_1 = "https://whatismyipaddress.com/"#"https://2ip.ru/"  #31.204.232.144 213.169.33.7
expected_url_2 = "https://2ip.ru/"
driver.get(expected_url_1)

# current_source = driver.page_source
# print(current_source)

sleep(5)