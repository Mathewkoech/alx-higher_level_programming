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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        """defines area of a square"""

    def area(self):
        """
        Area of the square
        Return: squared size that is area
        """
        return self.__size**2
