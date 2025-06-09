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
options.add_argument("--headless")
# этой опцией мы отключаем оповещение от браузера об автоконтроле
options.add_argument("--disable-blink-features=AutomationControlled")
#этой строкой мы меняем юзерагента для сервера
# если мы хотим юзать хедлесс мод и не отлетать по проверке на робота:
# задаем дизейбл блинк и юзер агента
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

# сайт для проверки юзерагента
# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html") #"https://hh.ru/")
driver.get("https://whatismyipaddress.com/")
wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))
# wait.until(EC.title_is("Какой у меня IP-адрес — см. ваш публичный адрес — IPv4 и IPv6"))
# time.sleep(5)
print("Title is find")
# так делаем скрины в ту же директорию с дефолтным именем
driver.save_screenshot("screen_1.png")