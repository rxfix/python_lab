__author__ = 'Нестеренко Александр'

# Задание 2 *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока
# nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для
# получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
# <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?


import urllib.request
import time
import re

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = urllib.request.urlopen(URL)

# reg_exp = ((?:[\d]{1,3}\.){3}[\d]{1,3}).*\[(.*)\].\"([A-Z]+).((?:\/\w+)*).*\".([\d]{1,3}).(\d+)
reg_exp = r"""
    ((?:[\d]{1,3}\.){3}[\d]{1,3}).*  # <remote_addr>
    \[(.*)\].  # <request_datetime>
    \"([A-Z]+).  #<request_type>
    ((?:\/\w+)*).*  # <requested_resource>
    \".([\d]{1,3}).  # <response_code>
    (\d+)  # <response_size>
    """
for raw in response:  # читаем по стокам из запроса
    parsed_raw = re.findall(reg_exp, str(raw), re.VERBOSE)
    print(parsed_raw)
    time.sleep(0.5)
