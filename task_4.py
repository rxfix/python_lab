__author__ = 'Нестеренко Александр'


# Задание 4.Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    is_police = False

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name

    def __str__(self):
        return f'{self.speed} {self.color} {self.name} {self.is_police}'

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} Машина поехала')

    def stop(self):
        self.speed = 0
        print(f'{self.name} Машина остановилась')

    @staticmethod
    def turn(direction):
        print(f'Машина повернула, {direction}')

    def show_speed(self):
        print(f'Текущая скорость:{self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if 60 < self.speed:
            print(f'Превышении скорости: {self.speed - 60}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if 40 < self.speed:
            print(f'Превышении скорости: {self.speed - 40}')


class PoliceCar(Car):
    is_police = True


if __name__ == '__main__':
    police_car = PoliceCar('blue', 'Alfa')
    town_car = TownCar('red', 'Audi')
    work_car = WorkCar('green', 'VW')

    print(police_car)
    print(town_car)
    print(work_car)

    police_car.go(80)
    police_car.show_speed()

    town_car.go(90)
    town_car.show_speed()

    work_car.go(50)
    work_car.show_speed()
