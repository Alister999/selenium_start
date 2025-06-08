import inspect
import time

from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

service = SafariService()
driver = webdriver.Safari(service=service)

expected_url = "https://saby.ru/"

driver.get(expected_url)
btns = driver.find_elements("class name", "sbisru-Button")
# btns = driver.find_elements("xpath", "//img")#div input span

btns[0].click()

time.sleep(3)

# Получаем все доступные окна
windows = driver.window_handles
# Переключаемся на последнее открытое окно (новая вкладка)
driver.switch_to.window(windows[-1])

inputs = driver.find_elements("xpath", "//input")

# print(driver.current_url)
# print(len(inputs))

# for i, elem in enumerate(inputs):
#     try:
#         if hasattr(elem, "text"):
#             # print(f"Text of {i} element - {elem.text}")
#             print(*inspect.getmembers(elem), sep="\n")
#             # print(dir(elem))
#             # print(elem.__dict__)
#         else:
#             print(f"Element {i} haven't text attribute")
#     except Exception as e:
#         print(f"Error - {e}")

# inputs[0].click()
inp = driver.find_elements("xpath", "//div[@data-qa='auth-Tabs__registerTab']")
# if inp[0]:
#     inp[0].click()
# так работает поиск по атрибуту, исключение - поиск по тексту
inp2 = driver.find_elements("xpath", "//div[text()='Регистрация']")
# inp[0].click()
# if inp2[0]:
#     inp2[0].click()
#это поиск по полному пути икспаф
inp3 = driver.find_element("xpath", '//*[@id="wasaby-content"]/div/div/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[2]')
# inp3.click()

#так же можем поискать по содержимому, например классам
inp4 = driver.find_elements("xpath", '//div[contains(@class, "auth-Tabs__tab")]')
# print(f'Div contains class auth-Tabs__tab {len(inp4)}p')
# inp4[1].click()
#и мы можем находить элементы по двум и более атрибутам
inp5 = driver.find_elements("xpath", '//div[@class="auth-Tabs__tab controls-margin_left-xl controls-padding_bottom-2xs" and @data-qa="auth-Tabs__registerTab"]')
inp5[0].click()

# btn.click()

time.sleep(2)