import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

list_items = []
i = 1
while i <= 3:
    driver.get(f"https://www.ozon.ru/category/smartfony-15502/?page=1&sorting=rating")
    wait = WebDriverWait(driver, timeout=15)
    wait.until(lambda b: b.find_element(By.XPATH, '//div[@class=\'y9c\'] '))
    time.sleep(3)
    button_next = driver.find_element(By.XPATH,
                                      '//div[text()=\'Дальше\' and @class=\'_4-e1\']//ancestor::a')  # Сначала находит кнопку Дальше и дальше ищет ближайшую ссылку в дереве к ней

    new_list_items = driver.find_elements(By.XPATH, '//div[@data-widget=\'searchResultsV2\']//div[@class=\'rk3 r3k\']')
    list_items.extend(new_list_items)
    ActionChains(driver).scroll_by_amount(0, 250).scroll_by_amount(0, 250).scroll_by_amount(0, 250).move_to_element(
        button_next).click(button_next)
    time.sleep(3)
    i += 1

list_of_smartphones_on_page_aTag = \
    [item.find_element(By.XPATH, './/a[@class=\'tile-hover-target k8n\']') for item in list_items[:100]]

list_urls = []
for item in list_of_smartphones_on_page_aTag:
    list_urls.append(item.get_attribute('href').split('?')[0])
print(list_urls)
#не доделал  переход по каждой ссылку и парсинг данных