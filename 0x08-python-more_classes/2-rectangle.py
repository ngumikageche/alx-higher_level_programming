#!/usr/bin/python3
""" Define a class Rectangle """


class Rectangle:
    """Represent a rectangle. """
    def __init__(self, width=0, height=0):
        """ Initialization of a new Rectangle
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        # assign the value to the __width
        self.__width = value

    @property
    def height(self):
        """get/set the width of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ func that returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ func that returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
