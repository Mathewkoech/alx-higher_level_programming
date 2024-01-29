#!/usr/bin/python3


class Rectangle:
    """Empty class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        return (self.width + self.height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for _ in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str[:-1]
