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
import yaml
import re

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = urllib.request.urlopen(URL)

all_lisl = []
for raw in response:  # читаем по стокам из запроса
    parsed_raw = re.findall(r"""
    ((?:\d+\.){3}\d+)  # <remote_addr>
    (?:(?:\s\-){2}\s\[)
    (\d+\/\w+\/(?:\d+:){3}\d+.+\d+)  # <request_datetime>
    (?:\]\s")
    (\w+)  #<request_type>
    (?:\s)
    ((?:\/\w+){0,10})  # <requested_resource>
    (?:\s\w+\/\d+\.\d+"\s)
    (\d+)  # <response_code>
    (?:\s)
    (\d+)  # <response_size>
    """, str(raw), re.VERBOSE)
    all_lisl.append(parsed_raw)
    print(raw)

# with open('all_lisl.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump(all_lisl, f)


