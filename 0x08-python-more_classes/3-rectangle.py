#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """rep a Rectangle """
    def __init__(self, width=0, height=0):
        """Initialization
        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set/get the width of the Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func that returns the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """func that returns the perimeter of the Rectanglr"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represent the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))
