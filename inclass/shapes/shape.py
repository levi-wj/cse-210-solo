import math

class Shape:
    def get_area(self):
       return 0 

class Square(Shape):
    def __init__(self, l):
        self.l = l
    
    def get_area(self):
        return self.l ** 2

class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def get_area(self):
        return self.h * self.w

class Triangle(Shape):
    def __init__(self, h, b):
        self.h = h
        self.b = b

    def get_area(self):
        return (self.h * self.b) / 2

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def get_area(self):
        return math.pi * self.r ** 2

class Cone(Shape):
    def __init__(self, r, h):
        self.r = r
        self.h = h
    
    def get_area(self):
        base = Circle(self.r)
        return base.get_area() * self.h / 3