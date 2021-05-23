import urllib.request

from requests import get
import sys
# file_1 = open('hello.txt', 'r', encoding='utf-8')
# # content = file_1.read()
# # print(content)
#
# # clean_content = content.replace('\n', ' ').replace('\r', ' ')
# # print(clean_content)
#
# # paragraphs = content.splitlines()
# # print(paragraphs)
#
# for line in file_1:
#    print(line)
# file_1.close()

# response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# content = response.content.decode(
#         encoding=response.encoding)
# print(response.text)

response = urllib.request.urlopen('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

# line = response.readline()
# print(line)
# line = response.readline()
# print(line)
# line = response.readline()
# print(line)
# line = response.readline()
# print(line)

print(type(response), sys.getsizeof(response))

for line in response:
       print(line)
#     print(file_1.readline())
# with open(response.text, encoding='utf-8') as file_1:
# txt = '''Пробуем записать в файл текст.
# Используем метод .write().'''
#
# with open('write_method.txt', 'w', encoding='utf-8') as f:
#    f.write(txt)
#
