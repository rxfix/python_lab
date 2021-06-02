__author__ = 'Нестеренко Александр'


# Задание 3.Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы
# «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Поное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f"Доход с учетом премии: {self._income['wage'] + self._income['bonus']}"


if __name__ == '__main__':
    person_1 = Position('Петр', 'Иванов', 'бухгалтер', 500, 100)
    print(person_1.get_full_name())
    print(person_1.get_total_income())
    # print(person_1._income)
