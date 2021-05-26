
import os

root_dir = './'

__step__ = 1
# # for file in os.listdir(root_dir):

# #     print(type(file))
# #     print(file, os.path.isdir(file))
# #     print(file, os.path.isfile(file))
#
# for item in os.scandir(root_dir):
#     print(type(item))
#     # print(dir(item))
#     print(item.name, item.is_file())
#     print(item.name, item.is_dir())
#     print(item.name, item.stat())

__step__ = 2
# for root, dirs, files in os.walk(root_dir):
#     # print(files)
#     # print(type(root))
#     for file in files:
#         # print(root, file)
#         f_path = os.path.join(root, file)
#         print(f_path, os.path.exists(f_path))
#         print(os.stat(f_path).st_size)
#         print(os.path.abspath(f_path))
#         print(os.path.split(f_path))

__step__ = 3
ROOT = os.path.abspath(os.path.join(__file__, '..'))
print(ROOT)
print(os.listdir(ROOT))

folder = r'C:\Users\user\AppData\Local\Programs\Python\Python39\Lib\site-packages\django'
django_dirs = [item
               for item in os.listdir(folder)
               if os.path.isdir(os.path.join(folder, item))]
print(django_dirs)

__создание_1000_файлов__ = 4
# import os
# import random
#
# folder = 'some_data'
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(10 ** 3):
#    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#    f_content = bytes(random.randint(0, 255)
#                      for _ in range(random.randrange(10 ** 5)))
#    with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#        f.write(f_content)

__Подсчет_файлов__ = 5
# import os
# from time import perf_counter
#
# folder = 'some_data'
# start = perf_counter()
# size_threshold = 15 * 2 ** 10
# small_files = [item
#               for item in os.listdir(folder)
#               if os.stat(os.path.join(folder, item)).st_size < size_threshold]
# print(len(small_files), perf_counter() - start)
# # 155 2.271335837
# start = perf_counter()
# small_files_2 = [item.name
#                  for item in os.scandir(folder)
#                  if item.stat().st_size < size_threshold]
# print(len(small_files_2), perf_counter() - start)
# print(small_files == small_files_2)
#
#
# import os
# from time import perf_counter
#
# folder = 'some_data'
# start = perf_counter()
# all_files = [item
#               for item in os.listdir(folder)]
# print(len(all_files), perf_counter() - start)
# # 1000 0.056053622000000025
# start = perf_counter()
# all_files_2 = [item.name
#                 for item in os.scandir(folder)]
# print(len(all_files_2), perf_counter() - start)
# print(all_files == all_files_2)


__методы_и_пути__ = 6

__создание_переименование_и_удаление_папок__ = 7

import os

dir_name = 'sample_dir'
if not os.path.exists(dir_name):
   os.mkdir(dir_name)

import os

dir_path = os.path.join('data', 'src')
if not os.path.exists(dir_path):
   os.makedirs(dir_path)

dir_path = os.path.join('data', '555')
if not os.path.exists(dir_path):
   os.makedirs(dir_path)
   print(dir_path)



import yaml
from pprint import pprint

with open('info.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)

import yaml

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_yaml = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)

with open('sw_templates.yaml') as f:
    print(f.read())