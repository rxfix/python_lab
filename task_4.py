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
    def __init__(self, speed=0, color='', name='', is_police=False, speed_limit=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ''
        self.speed_limit = speed_limit

    def __str__(self):
        return f'{self.speed} {self.color} {self.name} {self.is_police}'

    def go(self, speed):
        self.speed = speed
        return self.speed

    def stop(self):
        self.speed = 0
        return self.speed

    def turn(self, direction):
        self.direction = direction
        return self.direction

    def show_speed(self):
        return f'Текущая скорость:{self.speed}'


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed_limit < self.speed:
            f'Текущая скорость: {self.speed}, допустимая скорость: {self.speed_limit}: Превышении скорости: {self.speed - self.speed_limit}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed_limit < self.speed:
            print(
                f'Текущая скорость: {self.speed}, допустимая скорость: {self.speed_limit}: Превышении скорости: {self.speed - 40}')
        # return f'Текущая скорость:{self.speed}'


class PoliceCar(Car):
    pass


car_1 = Car(100, 'red', 'Alfa', True, 120)
town_car = TownCar(speed=100, color='red', name='Audi', is_police=False, speed_limit=60 )
work_car = WorkCar(speed=40, color='red', name='Audi', is_police=False, speed_limit=1)

print(car_1.turn('right'))
# print(work_car.show_speed())
print(work_car.show_speed())
