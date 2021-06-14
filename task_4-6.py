_author__ = 'Нестеренко Александр'


# Задание 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Задание 5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру (например, словарь).

# Задание 6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.


class Stock:
    def __init__(self):
        self.product = {}

    def add_to(self, equipment):
        self.product.setdefault(str(equipment), []).append(equipment)

    def extract(self, name):
        if self.product[name]:
            self.product.setdefault(name).pop(0)


class OfficeEquipment:
    units = 'USD'

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, Цена: {self.price} {self.units},' \
               f' Количество: {self.quantity}'


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, type_print):
        super().__init__(name, price, quantity)
        self.type_print = type_print

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, Цена: {self.price} {self.units},' \
               f' Количество: {self.quantity} Тип: {self.type_print}'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, resolution):
        super().__init__(name, price, quantity)
        self.resolution = resolution

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, Цена: {self.price} {self.units},' \
               f' Количество: {self.quantity} Разрешение: {self.resolution}'


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, copy_speed):
        super().__init__(name, price, quantity)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, Цена: {self.price} {self.units},' \
               f' Количество: {self.quantity} Скорость копирования: {self.copy_speed}'



if __name__ == '__main__':
    sklad = Stock()

    printer = Printer('hp', 330, 99, 'Лазерный')
    sklad.add_to(printer)
    printer= Printer('hp', 330, 99, 'Струйный')
    sklad.add_to(printer)
    printer = Printer('hp', 330, 98, 'Лазерный')
    sklad.add_to(printer)


    print(sklad.product)
    print(printer)
