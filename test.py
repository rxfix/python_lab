# import urllib.request
#
# from requests import get
# import sys
#
# # file_1 = open('hello.txt', 'r', encoding='utf-8')
# # # content = file_1.read()
# # # print(content)
# #
# # # clean_content = content.replace('\n', ' ').replace('\r', ' ')
# # # print(clean_content)
# #
# # # paragraphs = content.splitlines()
# # # print(paragraphs)
# #
# # for line in file_1:
# #    print(line)
# # file_1.close()
#
# # response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# # content = response.content.decode(
# #         encoding=response.encoding)
# # print(response.text)
#
# response = urllib.request.urlopen(
#     'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

# line = response.readline()
# print(line)
# line = response.readline()
# print(line)
# line = response.readline()
# print(line)
# line = response.readline()
# print(line)


# txt_lines = ['Пробуем записать в файл текст.\n',
#              'Используем метод .writelines().\n']
file_users = open('users.csv', 'r', encoding='utf-8')
user = file_users.readline()
file_hobby = open('hobby.csv', 'r', encoding='utf-8')
hobby = file_hobby.readline()

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    while user:
        if not hobby:
            hobby = None
            f.write(f'{user[:-1]}: {hobby}\n')
        else:
            f.write(f'{user[:-1]}: {hobby}')
        user = file_users.readline()
        hobby = file_hobby.readline()

# for line in file_users:
#    f.write(f'{line[:-1]}: {file_hobby.readline()}')
# # f.write(line2)
# users_hobby = open('users_hobby.txt', 'r', encoding='utf-8')
# users_hobby.close()
file_users.close()
file_hobby.close()
