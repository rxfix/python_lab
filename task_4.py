__author__ = 'Нестеренко Александр'


# Задание 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(is_valid):
    def wrapper(func):
        def validator(*args):
            if is_valid(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'wrong val:{args}')

        return validator

    return wrapper


def lam(x):
    return 0 < x


@val_checker(lam)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
