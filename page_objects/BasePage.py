import time
from transliterate import slugify
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from transliterate import translit

class BasePage(object):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def open(self, url=''):
        url = self.base_url + url
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def click_on_element(self, *locator):
        self.find_element(*locator).click()

    def wait_visible_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
            time.sleep(1)
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def wait_located_element(self, *locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(*locator)) # presence_of_element_located
            time.sleep(1)
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_new_window(self):
        handle = self.driver.window_handles
        for i in range(10):
            if len(handle) > 1:
                return True
            else:
                time.sleep(1)
        print("\n * NEW WINDOW NOT FOUND WITHIN GIVEN TIME! --> %s")
        return False

    def scroll_to_elem(self, *locator):
        for i in range(10):
            try:
                self.find_element(*locator)
                break
            except NoSuchElementException:
                if i < 10:
                    ActionChains(self.driver).scroll_by_amount(0, 680).perform()
                    continue
                else:
                    raise NoSuchElementException


    def check_strong_city(self, city_name:str, *locator):
        city = self.find_element(*locator).text
        if city_name in city:
            return True
        return False


    def check_other_city(self, locator_left, locator_right):
        left_column = self.find_elements(locator_left)
        right_column = self.find_elements(locator_right)
        if len(left_column) > 0 and len(right_column) > 0:
            left_cities = [city.text for city in left_column]
            right_cities = [city.text for city in right_column]
            return left_cities == right_cities
        else: raise NoSuchElementException


    def check_url_city(self, city_name):
        url = self.driver.current_url
        return slugify(city_name) in url

