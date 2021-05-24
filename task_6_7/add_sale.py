__author__ = 'Нестеренко Александр'

import sys


def rec(_summa):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{_summa}\n')


if len(sys.argv) < 2:
    print('Введите в терминале сумму продаж, например: "add_sale.py 123.4"')
else:
    result = rec(sys.argv[1])
    print('записанная сумма продаж:', sys.argv[1])
