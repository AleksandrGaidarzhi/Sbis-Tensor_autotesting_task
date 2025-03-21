import os
import urllib.request

from page_objects.BasePage import BasePage


class SbisMainPage(BasePage):
    def switch_window(self):
        handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(handle)

    def scroll_footer(self, *locator):
        footer = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView()", footer)

    def download_element(self, locator):
        links = self.driver.find_elements(*locator)
        url = links[0].get_property('href')
        text = links[0].get_property('text')
        exp_file_size = float(text.split(' ')[-3])
        filename = url.split('/')[-1]
        urllib.request.urlretrieve(url, filename)
        return filename, exp_file_size


    def file_remove(self, file_name):
        try:
            os.remove(file_name)
        except Exception:
            pass

    def check_file_size(self, file_name, exp_file_size):
        real_size_b = os.path.getsize(file_name)
        real_size_mb = round((real_size_b / 1024) / 1024, 2)
        # self.file_remove(file_name)  # удаление файла после теста, отключена т.к. нет в ТЗ
        return exp_file_size == real_size_mb

    @staticmethod
    def check_file_exist(file_name):
        return os.path.exists(file_name)



