__author__ = 'Нестеренко Александр'

# Задание 1. # Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# Задание 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

import urllib.request

from requests import get
import sys

response = urllib.request.urlopen(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

slovar = {}
for line in response:
    spammer_ip = str(line).split(' - - ')[:1]  # ["b'173.255.199.22"]
    # print(spammer_ip)
    if slovar.get(spammer_ip[0]):
        slovar[spammer_ip[0]] += 1
    else:
        slovar.setdefault(spammer_ip[0], 1)

n = 0
for key in slovar:
    if slovar[key] > n:
        n = slovar[key]
        spammer = key[2:]
        print(n)
    # print(slovar[key])

print(slovar)
print(sys.getsizeof(slovar))
print(type(response), sys.getsizeof(response))
print(spammer)
