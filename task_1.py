__author__ = 'Нестеренко Александр'

# Задание 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных
# папках и файлах (добавлять детали)?
# Задание 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#
#
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом
# редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки
# использовать нельзя.

import os
import yaml


def create_dir(path):
    if not os.path.exists(path):  # если директории не существует
        os.makedirs(path)  # создать директорию


def create_file(path, file_name):
    file_path = os.path.join(path, str(file_name))
    if not os.path.exists(file_path):  # если файла не существует
        with open(file_path, 'w', encoding='utf-8') as f:  # создать файл
            f.write('')


def create_starter(config_file):
    with open(config_file) as f_structure:
        structure = yaml.safe_load(f_structure)

    for key_path, val_files_names in structure.items():  # ключи структуры - директории
        create_dir(key_path)
        if val_files_names:  # списки значений - имена файлов
            for file_name in val_files_names:
                create_file(key_path, file_name)


if __name__ == '__main__':
    create_starter('config.yaml')
