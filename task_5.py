__author__ = 'Нестеренко Александр'

# Задание 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей
# (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

# Задание 5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в
# котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import json


def get_key(_size):
    num_digits = 1
    while _size // 10:
        num_digits += 1
        _size //= 10
    return 10 ** num_digits


def get_dirs(_root_dir):
    stat_dic = {}
    for root, _, files in os.walk(_root_dir):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            key = get_key(size)
            ext = file.split('.')[-1]
            try:
                stat_dic[key][0] += 1
                ext_list = stat_dic[key][1]
                if ext in ext_list:
                    pass
                else:
                    ext_list.append(ext)
            except (KeyError, IndexError):
                stat_dic[key] = [1, [ext]]
    return stat_dic


root_dir = './'

if __name__ == '__main__':
    with open('summary.json', 'w', encoding='utf-8') as f:
        json.dump(get_dirs(root_dir), f)
