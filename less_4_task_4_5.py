__author__ = 'Нестеренко Александр'

# Задание 4.Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

# Задание 5. Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import sys
import utils

print(sys.argv[1:])
print(utils.currency_rates('usD'))
print(utils.currency_rates('JpY'))
print(utils.currency_rates('EUR'))
