import random
from selenium import webdriver
import pytest
from page_objects.sbis_main_page import SbisMainPage
from utils.locators import SbisMainPageLocators as sbis_main_loc
from utils.locators import SbisContactPageLocators as sbis_cont_loc
from utils.locators import TensorMainPageLocators as tens_mp_loc
from utils.locators import TensorAboutPageLocators as tens_ab_loc
from utils.locators import SbisDownloadPageLocators as sbis_dl_loc




@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    browser.implicitly_wait(6)
    yield browser
    print("\nquit browser..")
    browser.quit()

'''
В реальном тестировании мы бы разбили сценарий на серию кейсов сгруппировав их по одному 
из признаков (эндпоинту или исходя из принадлежности тестируемых элементов к какой-либо сущности).
Но так как это учебное задание и в условии это не требуется - рассматриваем один сценарий как один кейс.
'''


class TestTaskAQA:
    SBIS_URL = 'https://sbis.ru/'
    TENSOR_URL = 'https://tensor.ru/'
    TENSOR_ABOUT = 'https://tensor.ru/about'

    def test_first_scenario(self, browser):
        page = SbisMainPage(browser, self.SBIS_URL)
        page.open()
        page.wait_visible_element(sbis_main_loc.CONTACT_HEAD)
        page.click_on_element(sbis_main_loc.CONTACT_HEAD)
        page.click_on_element(sbis_main_loc.CONTACT_GO)
        page.wait_located_element(sbis_cont_loc.TENSORBANNER)
        page.click_on_element(sbis_cont_loc.TENSORBANNER)
        page.wait_new_window()
        page.switch_window()
        page.wait_visible_element(tens_mp_loc.TENSOR_TITLE)
        assert  page.get_url() == self.TENSOR_URL
        page.scroll_to_elem(tens_mp_loc.PEOPLES_POWER)
        page.click_on_element(tens_mp_loc.PEOPLE_MORE)
        assert page.get_url() == self.TENSOR_ABOUT

        page.scroll_to_elem(tens_ab_loc.PHOTOS_WORKING)
        title = page.find_element(tens_ab_loc.TITLE_WORKING)
        assert title.text == 'Работаем'
        images = page.find_elements(tens_ab_loc.PHOTOS_WORKING)
        assert all(images[0].size == image.size for image in images)

    def test_second_scenario(self, browser):
        page = SbisMainPage(browser, self.SBIS_URL)
        page.open()
        page.wait_visible_element(sbis_main_loc.CONTACT_HEAD)
        page.click_on_element(sbis_main_loc.CONTACT_HEAD)
        page.click_on_element(sbis_main_loc.CONTACT_GO)
        page.wait_visible_element(sbis_cont_loc.CONTACT_LIST)
        my_city = page.find_element(sbis_cont_loc.CHOOSEN_CITY).text

        '''
        Т.к. город определяется автоматически (по IP), то тест должен работать корректно откуда бы его не запускали
        и в ТЗ на этот счет нет указаний (Ярославская область приведена для примера)
        поэтому реализована проверка для всех городов/регионов хоть и ТЗ этого не требует
        '''

        if my_city in ['Москва', 'Санкт-Петербург']:  # если наш город Москва или Питер, то верстка одна
            result = page.check_strong_city(my_city, sbis_cont_loc.STRONG_OFFICE_CITY)
            assert result is True
        else:
            # Если город из регионов, то верстка другая (города и офисы расположены в колонках)
            result = page.check_other_city(sbis_cont_loc.OTHER_CITIES_LEFT, sbis_cont_loc.OTHER_CITIES_RIGHT)
            assert result is True

        page.click_on_element(sbis_cont_loc.CHOOSEN_CITY)
        page.wait_located_element(sbis_cont_loc.REGION_SELECT)
        city_list = page.find_elements(sbis_cont_loc.OTHER_CITIES_CHOSE)  # сбор остальных регионов
        random.choice(city_list).click()  # рандомно выбираем один из них
        page.wait_visible_element(sbis_cont_loc.CONTACT_LIST)
        result = page.check_other_city(sbis_cont_loc.OTHER_CITIES_LEFT, sbis_cont_loc.OTHER_CITIES_RIGHT)  # чекаем города региона
        assert result is True

        curr_city_name = page.find_element(sbis_cont_loc.CHOOSEN_CITY).text
        partners = page.find_elements(sbis_cont_loc.PARTNERS)
        curr_partners = [partnr.text for partnr in partners]

        page.click_on_element(sbis_cont_loc.CHOOSEN_CITY)
        page.wait_visible_element(sbis_cont_loc.REGION_SELECT)
        city_list = page.find_elements(sbis_cont_loc.OTHER_CITIES_CHOSE)
        new_city = city_list[4]
        '''
        Проверяем не совпал ли наш выбор с предыдущим (случайным), если совпал - меняем.
        Лучше было бы генерировать два случайных числа отличных друг от друга и 
        при каждом запуске теста сравнивать страницы разных регионов
        '''
        if curr_city_name in new_city.text:
            new_city = city_list[12]
        new_city_name_whole = new_city.text
        new_city.click()
        page.wait_visible_element(sbis_cont_loc.CONTACT_LIST)

        new_city_name = page.find_element(sbis_cont_loc.CHOOSEN_CITY).text
        partners = page.find_elements(sbis_cont_loc.PARTNERS)
        new_partners = [partnr.text for partnr in partners]

        assert new_city_name in new_city_name_whole
        assert new_city_name != curr_city_name
        assert new_partners != curr_partners
        '''
        Проверка соответствия региона на странице и в URL.
        Для транслитерации названия региона в URL нужно использовать тот же инструмент,
        который использовался разработчиками. Т.к. нам неизвестно как генерировали названия регионов - использовалась
        библиотеку transliterate. Существует несколько подходов транслитерации (можно в т.ч. создавать свои правила),
        поэтому метод ненадежный. В реальном проекте нужно использовать ту же библиотеку что используют разработчики,
        либо делать таблицу соответствия и искать по ней (хуже с точки зрения поддержки).        '''

        assert page.check_url_city(new_city_name) is True

    def test_third_scenario(self, browser):
        page = SbisMainPage(browser, self.SBIS_URL)
        page.open()
        page.scroll_footer(sbis_main_loc.FOOTER_FIND)
        page.wait_located_element(sbis_main_loc.FOOTER_DOWNLOAD)
        page.click_on_element(sbis_main_loc.FOOTER_DOWNLOAD)
        filename, exp_file_size = page.download_element(sbis_dl_loc.DOWNLOAD_LINK)
        assert page.check_file_exist(filename) is True
        assert page.check_file_size(filename, exp_file_size) is True
        # файл скачивается в папку test согласно ТЗ. Также реализовано удаление файла после теста, но закомментировано
        # так как нет в ТЗ и возможно вы захотите проверить файл вручную



























        




