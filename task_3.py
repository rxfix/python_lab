__author__ = 'Нестеренко Александр'

# Задание 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками»
# в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в
# родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные
# ситуации; это реальная задача, которая решена, например, во фреймворке django.
import os
from shutil import copyfile


def get_dirs(project_root, dir_name):  # поиск путей к нужным директориям
    required_dirs = set()
    for root, dirs, _ in os.walk(project_root):
        for _dir in dirs:
            if _dir == dir_name:
                required_dirs.add(os.path.join(root, _dir))
    return required_dirs


def copi_dir(scr, dst):  # копирование содержимого найденных директорий
    for _dir in scr:
        for root, dirs, files in os.walk(_dir):
            for file in files:
                dir_name = os.path.join(dst, os.path.basename(root))
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                if not os.path.exists(os.path.join(dir_name, file)):
                    copyfile(os.path.join(root, file), os.path.join(dir_name, file))


root_dir = './my_project'
required_dir = 'templates'
destination_dir = './my_project/templates'

if __name__ == '__main__':
    source_dir = get_dirs(root_dir, required_dir)
    copi_dir(source_dir, destination_dir)
