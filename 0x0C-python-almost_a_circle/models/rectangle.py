#!/usr/bin/python3
"""Defines a rectangle class that inherits Base class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class
        Args:
            width (int): The width.
            height (int): The height .
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The new Rectangle identity.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either  width or height <= 0.
            TypeError: If either  x or y is not an int.
            ValueError: If either x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.width = width
        self.__height = height
        self.height = height
        self.__x = x
        self.x = x
        self.__y = y
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width
        Args:
            width: parameter
        Raises:
            TypeError: if width not int
            ValueError: if width less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height
        Args:
            height: parameter
        Raises:
            TypeError: if height not int
            ValueError: if height less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x
        Args:
            x: parameter
        Raises:
            TypeError: if x not int
            ValueError: if x less than 0
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y
        Args:
            y: parameter
        Raises:
            TypeError: if y not int
            ValueError: if y less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
        *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents width attribute
            - 3rd argument represents height attribute
            - 4th argument represents x attribute
            - 5th argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
