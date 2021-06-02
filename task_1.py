__author__ = 'Нестеренко Александр'

# Задание 1. Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) —
# 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить
# соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    def __init__(self, color='красный'):
        self.__color = color
        self.__times = {'красный': 7, 'жёлтый': 2, 'зелёный': 5}

    def __str__(self):
        return f'{self.__color}'

    def running(self):
        for _ in range(3):
            print(self.__color)
            time.sleep(self.__times[self.__color])
            if self.__color == 'красный':
                self.__color = 'жёлтый'
            elif self.__color == 'жёлтый':
                self.__color = 'зелёный'
            else:
                self.__color = 'красный'


if __name__ == '__main__':
    traffic_light_1 = TrafficLight()
    traffic_light_1.running()

