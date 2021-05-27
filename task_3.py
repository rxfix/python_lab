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


def copi_dir(scr, dst):
    pass


def get_dirs(project_root, dir_name):  # поиск путей к нужным директориям
    required_dirs = set()
    for path, dirs, _ in os.walk(project_root):
        for dir in dirs:
            if dir == dir_name:
                required_dirs.add(os.path.join(path, dir))
    return required_dirs


def gather_templates(root):
    pass


root = './my_project'
required_dir = 'templates'


print(get_dirs(root, required_dir))
