#!/usr/bin/python3
"""Shapes with Abstract Base Classes"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract Shape Class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Circle Shape"""

    def __init__(self, radius):
        if isinstance(radius, (int, float)):
            self.radius = abs(radius)

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    """Rectangle Shape"""

    def __init__(self, width=0, height=0):
        if isinstance(width, (int, float)):
            self.width = width
        if isinstance(height, (int, float)):
            self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    """Print shape's area and perimeter"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    shape_info(circle)
    shape_info(rectangle)
