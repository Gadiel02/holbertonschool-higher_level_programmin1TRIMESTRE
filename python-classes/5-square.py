#!/usr/bin/python3
"""Defines a square"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)

# Ejemplo de uso:
if __name__ == "__main__":
    s = Square(3)
    s.my_print()
    print(f"Area: {s.area()}")
    s.size = 5
    s.my_print()
    print(f"Area: {s.area()}")
