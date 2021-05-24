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

response = urllib.request.urlopen(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

# создание словаря с ip и их повторений
spammer_dic = {}
for line in response:
    line_ip = str(line).split(' - - ')  # ["b'173.255.199.22"]
    if spammer_dic.get(line_ip[0]):  # если ip есть в словаре, добавляем +1 в значение по ключю
        spammer_dic[line_ip[0]] += 1
    else:
        spammer_dic.setdefault(line_ip[0], 1)  # если ip нет в словаре, то добавляем его в словарь
        # как ключ и устанавливаем значение по ключю как 1

# поиск спамера
spammer_ip = ''
max_request = 0
for key in spammer_dic:
    if spammer_dic[key] > max_request:
        max_request = spammer_dic[key]
        spammer_ip = key

print(f'IP адрес спамера: {spammer_ip[2:]}, который сделал {max_request} запросов.')
