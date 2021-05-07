# class Auto:
#     # атрибуты класса
#     auto_name = "Lexus"
#     auto_model = "RX 350L"
#     auto_year = 2019
#
#     # методы класса
#     def on_auto_start(self):
#         print(f"Заводим автомобиль")
#
#     def on_auto_stop(self):
#         print("Останавливаем работу двигателя")
#
# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_auto_start()
# a.on_auto_stop()
#
# Разберёмся
# на
# примере.
#

################
#
# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
# a = Auto()
# a.on_auto_start("Lexus", "RX 350L", 2019)
# print(a.auto_name)
# print(a.auto_count)
#
# a_2 = Auto()
# a_2.on_auto_start("Mazda", "CX 9", 2018)
# print(a_2.auto_name)
# print(a_2.auto_count)
#

#############


# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # методы класса
#     def __init__(self):
#         Auto.auto_count += 1
#         print(Auto.auto_count)
#
# a_1 = Auto()
# a_2 = Auto()
# a_3 = Auto()



##############

# class Auto:
#
#     def get_class_info(self):
#         print("Детальная информация о классе")
#
#
# a = Auto()
# a.get_class_info()



################
class Auto:
    def on_start(self):
        info = "Автомобиль заведен"
        return info

a = Auto()
print(a.info)
