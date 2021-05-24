import sys
if len(sys.argv) == 0:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        f.write(f'{_summa}\n')
