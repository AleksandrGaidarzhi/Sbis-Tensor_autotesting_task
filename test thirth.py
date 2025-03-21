import time
from time import process_time_ns

from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.implicitly_wait(5)

browser.get('https://tensor.ru/about')
time.sleep(3)



# element = browser.find_element(By.XPATH, '//div[contains(text(), "Миссия и ценности")]')
# browser.execute_script("arguments[0].scrollIntoView()", element)
# time.sleep(5)
# element = browser.find_element(By.XPATH, '//div[contains(text(), "Миссия и ценности")]')
# browser.execute_script("arguments[0].scrollIntoView()", element)

# page = browser.find_element(By.XPATH, '//h2[contains(text(), "Работаем")]')
# print(page.text)
# page = browser.find_element(By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
# print(page)
# def find_everthing():
#     for i in range(10):
#         try:
#             browser.find_element(By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
#             break
#         except NoSuchElementException:
#             if i < 10:
#                 ActionChains(browser).scroll_by_amount(0, 680).perform()
#                 continue
#             else:
#                 raise NoSuchElementException
#
#
# find_everthing()
# img = browser.find_elements(By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
# print(img)



# for i in range(1,4):
#     try:
#         browser.find_element(By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
#         break
#     except (WebDriverException, NoSuchElementException):
#         ActionChains(browser).scroll_by_amount(0, 650).perform()
#         continue
#     else: raise NoSuchElementException


# hover = ActionChains(browser).scroll_by_amount(0, 800)
# hover.perform()
# hover = ActionChains(browser).scroll_by_amount(0, 800)
# hover.perform()

# time.sleep(1)