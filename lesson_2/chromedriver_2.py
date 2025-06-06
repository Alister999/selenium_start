from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())#либа для работы с драйвером, здесь указываем не бинарник а устангвленный драйвер
#В управляющую сервайс которая открывает - закрывает работу прокидываем установленный вебдрайвер
driver = webdriver.Chrome(service=service)
#Инициализируем драйвер

driver.get("https://vm619644.eurodir.ru")