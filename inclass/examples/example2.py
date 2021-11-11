class Shape:
    def __init__(self):
        self.name = "Unknown"

    def get_area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, h, w):
        self.__h = h
        self.__w = w

    def get_area(self):
        return self.__h * self.__w

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

aSquare = Square(10)
print(aSquare.name)
