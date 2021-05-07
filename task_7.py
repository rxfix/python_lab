_author__ = 'Нестеренко Александр'


# Задание 7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))


if __name__ == '__main__':
    num_1 = ComplexNumber(2, 3)
    num_2 = ComplexNumber(-1, 8)
    num_3 = ComplexNumber(3, 4)
    print(num_1 + num_2 + num_3)
    print(num_1 * num_2 * num_3)
