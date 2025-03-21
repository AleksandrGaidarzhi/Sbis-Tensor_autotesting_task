from selenium.webdriver.common.by import By


class SbisMainPageLocators(object):
    CONTACT_HEAD = (By.XPATH, '//div[contains(text(), "Контакты")]')
    CONTACT_GO = (By.XPATH, '//span[contains(text(), "офисов в регионе")]')
    FOOTER_FIND = (By.XPATH, '//div[@class="sbisru-Footer sbisru-Footer__scheme--default"]')
    FOOTER_DOWNLOAD = (By.XPATH, '//li[@class="sbisru-Footer__list-item pb-16"]/a[contains(text(), "Скачать локальные версии")]')

class SbisDownloadPageLocators(object):
    DOWNLOAD_LINK = (By.XPATH,'//a[@class="sbis_ru-DownloadNew-loadLink__link js-link"]')


class SbisContactPageLocators(object):
    TENSORBANNER = (By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]')
    POWER_BLOCK = (By.CLASS_NAME, 'tensor_ru-Index__block4-content tensor_ru-Index__card')
    POWER_TITLE = (By.XPATH, '//p[contains(text(), "Сила в людях")]')
    POWER_DETAILS = (By.CLASS_NAME, 'tensor_ru-link tensor_ru-Index__link')
    CHOOSEN_CITY = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    STRONG_OFFICE_CITY = (By.XPATH, '//div[@class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32" and @itemprop="name"]')
    OTHER_CITIES_CHOSE = (By.XPATH, '//li[@class="sbis_ru-Region-Panel__item"]')
    STRONG_CITIES_CHOSE = (By.XPATH, '//li[@class="sbis_ru-Region-Panel__item sbis_ru-Region-Panel__item--strong"]')
    OTHER_CITIES_RIGHT = (By.XPATH, '//div[@class="sbisru-Contacts-List__city sbisru-text--standart sbisru-Contacts__text--500 sbisru-Contacts__text--md-xm pl-24 pl-xm-0 pt-16 pt-xm-12 pb-4 pb-xm-8 ws-flexbox ws-justify-content-between ws-align-items-start"]')
    OTHER_CITIES_LEFT = (By.XPATH, '//div[@class="sbisru-Contacts-City__item-name sbisru-link pr-4 pr-xm-8 sbisru-text-main"]')
    CONTACT_LIST = (By.XPATH, '//div[@id="contacts_list"]')
    REGION_SELECT = (By.XPATH, '//div[@class="sbis_ru-Region-Panel__header ws-flexbox ws-justify-content-between ws-flex-wrap ws-align-items-baseline"]')
    PARTNERS = (By.XPATH, '//div[@class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]')


class TensorMainPageLocators(object):
    TENSOR_TITLE = (By.XPATH, '//h1[@class="tensor_ru-Index__Banner-title"]')
    PEOPLE_BLOCK = (By.CLASS_NAME, 's-Grid-container tensor_ru-Index__block4')
    PEOPLES_POWER = (By.XPATH, '//p[contains(text(), "Сила в людях")]')
    PEOPLE_MORE = (By.XPATH, '//a[contains(text(), "Подробнее") and @href="/about"]')

class TensorAboutPageLocators(object):
    BLOCK_WORKING = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')
    TITLE_WORKING = (By.XPATH, '//div[@class="tensor_ru-About__block-title-block"]/h2[@class="tensor_ru-header-h2 tensor_ru-About__block-title"]')
    PHOTOS_WORKING = (By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')

