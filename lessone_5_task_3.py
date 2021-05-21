__author__ = 'Нестеренко Александр'

# # Задание 3.
# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше
# элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких
# ситуациях генератор даст эффект.

import sys

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Александр', 'Евгений', 'Борис'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def tutors_klasses_gen(_tutors, _klasses):
    for item in range(len(_tutors)):
        if item >= len(_klasses):  # если длина списока tutors больше длины списка klasses
            yield _tutors[item], None  # ('Евгений', None)
        else:
            yield _tutors[item], _klasses[item]  # ('Иван', '9А')


tutors_klasses_gen_tuple = tutors_klasses_gen(tutors, klasses)

for _ in range(len(tutors)):
    print(next(tutors_klasses_gen_tuple))
print(type(tutors_klasses_gen_tuple), sys.getsizeof(tutors_klasses_gen_tuple))
