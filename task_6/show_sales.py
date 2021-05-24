__author__ = 'Нестеренко Александр'

import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) < 2:  # просто запуск скрипта — выводить все записи
        for line in f:
            print(str.strip(line))
    if len(sys.argv) == 2:  # запуск скрипта с одним параметром-числом — выводить все записи с номера,
        # равного этому числу, до конца
        for _ in range(int(sys.argv[1]) - 1):  # пропускаем строки до нужной записи
            f.readline()
        for line in f:  # выводим все записи с номера, равного этому числу, до конца
            print(str.strip(line))
    if len(sys.argv) == 3:  # запуск скрипта с двумя числами — выводить записи, начиная с номера,
        # равного первому числу, по номер, равный второму числу, включительно
        for _ in range(int(sys.argv[1]) - 1):  # пропускаем строки до нужной записи
            f.readline()
        for _ in range(int(sys.argv[2])-int(sys.argv[1]) +1):  # выводим все записи с номера, равного этому числу, по номер,
            # равный второму числу, включительно.
            print(str.strip(f.readline()))
