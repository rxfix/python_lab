__author__ = 'Нестеренко Александр'


# Задание 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести
# тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать
# работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(func):
    def wrapper(*args):
        result = func(*args)
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})')
        print(f'{func.__name__}: {type(result)}')
        return result

    return wrapper


@type_logger
def calc_cube(x, y, z):
    return x ** 3 + y, z


print(calc_cube(3, 4.5, '5'))
