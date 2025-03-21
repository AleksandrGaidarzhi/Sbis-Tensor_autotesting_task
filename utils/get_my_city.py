import requests


try:
    page = requests.get('https://2ip.ru/')
except Exception:
    page = requests.get('https://2ip.ru/')

page = page.text.split('title="Посмотреть точное место на карте"')
print(page)



