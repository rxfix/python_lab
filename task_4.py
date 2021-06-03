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
    def __init__(self, speed=0, color='', name='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ''

    def __str__(self):
        return f'{self.speed} {self.color} {self.name} {self.is_police}'

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула, {direction}')

    def show_speed(self):
        print(f'Текущая скорость:{self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if 60 < self.speed:
            print(f'Превышении скорости: {self.speed - 60}')
        else:
            return f'{self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if 40 < self.speed:
            print(f'Превышении скорости: {self.speed - 40}')
        else:
            print(f'Текущая скорость: {self.speed}')

class PoliceCar(Car):
    pass


if __name__ == '__main__':
    car_1 = Car(100, 'blue', 'Alfa', True)
    car_2 = TownCar(speed=50, color='red', name='Audi', is_police=False)
    car_3 = WorkCar(speed=40, color='green', name='VW', is_police=False)

    # print(car_1)
    # print(car_2)
    # print(car_3)
    # print(f'car_1: {car_1.show_speed()}')
    # print(car_2.show_speed())
    print(car_3.show_speed())
