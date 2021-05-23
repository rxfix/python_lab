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

# response = urllib.request.urlopen('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# slovar = {}
# for line in response:
#        spammer_ip = str(line).split(' - - ')[:1]  # ["b'173.255.199.22"]
#        # print(spammer_ip)
#        if slovar.get(spammer_ip[0]):
#               slovar[spammer_ip[0]] += 1
#        else:
#               slovar.setdefault(spammer_ip[0], 1)
# print(slovar)
# print(sys.getsizeof(slovar))
# print(type(response), sys.getsizeof(response))
# n=0
# for key in slovar:
#        if slovar[key] > n:
#               n=slovar[key]
#               spammer= key[2:]
#               print(n)
#        # print(slovar[key])

# print(slovar)
# print(sys.getsizeof(slovar))
# print(type(response), sys.getsizeof(response))
# print(spammer)
#

# txt = '''
# Пробуем записать в файл текст.
# Используем метод .write().'''
#
# with open('write_method.txt', 'a', encoding='utf-8') as f:
#    f.write(txt)


file_1 = open('users.csv', 'r', encoding='utf-8')
line1 = file_1.readline()
# while line:
#    print(line)
#    line = file_1.readline()
print(line1)
file_2 = open('hobby.csv', 'r', encoding='utf-8')
line2 = file_2.readline()
# while line:
#    print(line)
#    line = file_1.readline()
print(line2)


# txt_lines = ['Пробуем записать в файл текст.\n',
#              'Используем метод .writelines().\n']

with open('writelines_method.txt', 'a', encoding='utf-8') as f:
   f.write(f'{line1[:-1]}: {line2}')
   # f.write(line2)

file_1.close()
file_2.close()

