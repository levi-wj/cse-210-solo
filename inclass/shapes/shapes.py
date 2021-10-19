from shape import *

shapes = [
    Circle(8.0),
    Triangle(10.0, 5.0),
    Square(12.0),
    Rectangle(10.0, 11.0),
    Cone(14.0, 5.0)
]

sum = 0
for shape in shapes:
    area = shape.get_area()

    sum += area
    print(f'The area of the {type(shape).__name__} is {area}')

print(f'The total area is {sum}')