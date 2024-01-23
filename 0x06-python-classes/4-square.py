#!/usr/bin/python3
"""square module"""


class Square:
    """
    Square class defines a square with a private instance attribute 'size'.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Size of square
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

        """defines area of a square"""

    def area(self):
        """
        Area of the square
        Return: squared size that is area
        """
        return self.__size**2
