__author__ = 'Нестеренко Александр'

# Задание 4.Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

# Задание 5. Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05


import utils
import argparse

# Парсер для параметров командной строки
parser = argparse.ArgumentParser(description='Курс валюты по отношению к рублю, на текущюю дату')
# ArgumentParser (parser) - объект хранящий всю информацию , необходимую для разбора командной строки
parser.add_argument('currency', type=str, help='Название валюты')
# add_argument - добавление информации об аргументах в объект parser
args = parser.parse_args()  # анализ аргументов через parse_args()


if __name__ == '__main__':  # эта часть не будет выполняться при вызове этого модуля
    print(args.currency)
    if utils.currency_rates(args.currency):  # если результат функции найденная валюта и курс
        print(f'{utils.currency_rates(args.currency)[0]}, {utils.currency_rates(args.currency)[1]}')
        # print(type(utils.currency_rates(args.currency)[0])) # <class 'decimal.Decimal'>
        # print(type(utils.currency_rates(args.currency)[1])) # <class 'datetime.date'>
    else:
        print(utils.currency_rates(args.currency))  # если результат функции None
