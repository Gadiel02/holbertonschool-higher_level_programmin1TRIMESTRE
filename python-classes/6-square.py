#!/usr/bin/python3
"""Defines a square"""

class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(i, int) or i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

# Ejemplo de uso:
if __name__ == "__main__":
    s = Square(3, (1, 2))
    s.my_print()
    print(f"Area: {s.area()}")
    s.size = 5
    s.position = (2, 1)
    s.my_print()
    print(f"Area: {s.area()}")
