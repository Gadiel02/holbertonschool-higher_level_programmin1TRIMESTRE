#!/usr/bin/python3
"""Defines a square"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size  # This will call the setter method

    def area(self):
        """Returns current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
