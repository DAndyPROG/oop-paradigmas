from abc import ABC, abstractmethod

import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height


rectangle = Rectangle(3, 4)
circle = Circle(5)

print(f'Площа прямокутника: {rectangle.get_area()}')
print(f'Площа кола: {circle.get_area()}')
