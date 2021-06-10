# result = []
# for item in range(len(self.matrix)):
#     row = []
#     for cell in range(len(self.matrix[item])):
#         row.append(self.matrix[item][cell] + other.matrix[item][cell])
#     result.append(row)
# # return Matrix(result)


# result = []
# for row in self.matrix:
#     result.append(' '.join(map(str, row)))
# return '\n'.join(result)

class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя")

    def my_method(self):
        print("Метод my_method() класса ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        print("Конструктор дочернего класса")
        super().__init__()

    def my_method(self):
        super().my_method()
        print("Метод my_method() класса ChildClass")


c = ChildClass()
c.my_method()
