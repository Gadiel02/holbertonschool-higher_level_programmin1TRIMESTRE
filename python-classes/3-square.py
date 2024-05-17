#!/usr/bin/python3
"""Defines a square"""

class Square:
    """Initializes the data"""

    def __init__(self, size=0):
        """Initializes the data"""
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area"""
        return self.__size ** 2
