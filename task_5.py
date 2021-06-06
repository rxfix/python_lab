__author__ = 'Нестеренко Александр'


# Задание 5.Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен
# выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f'{self.title}'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисую ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисую караднашом')


class Handle(Stationery):
    def draw(self):
        print('Рисую маркером')


if __name__ == '__main__':
    pen = Pen("Ручка")
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')

    print(pen)
    pen.draw()
    print(pencil)
    pencil.draw()
    print(handle)
    handle.draw()
