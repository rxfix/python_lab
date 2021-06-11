__author__ = 'Нестеренко Александр'

# Задание 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption() + other.consumption()


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    def consumption(self):
        return self.h * 2 + 0.3


if __name__ == '__main__':
    coat_1 = Coat(187)
    suit_1 = Suit(150)
    c = coat_1 + suit_1
    print(coat_1.consumption())
    print(suit_1.consumption())
    print(c)
