__author__ = 'Нестеренко Александр'


# Задание 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = data
        self.validator(self.data)

    def __str__(self):
        return f'{self.data}'

    @classmethod
    def split_data(cls, data):
        data_list = []
        for item in data.split('-'):
            data_list.append(int(item))
        return cls(data_list)

    @staticmethod
    def validator(data_list):
        day, month, year = data_list
        if not (1 <= day <= 31):
            raise ValueError(f'wrong day')
        if not (1 <= month <= 12):
            raise ValueError(f'wrong month')
        return data_list


if __name__ == '__main__':
    day_1 = Data.split_data('14-12-2021')
    print(day_1)
    day_2 = Data([6, 11, 2021])
    print(day_2)
