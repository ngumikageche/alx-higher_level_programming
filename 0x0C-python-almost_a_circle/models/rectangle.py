#!/usr/bin/python3
"""Defines a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """body of rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int):The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getters and setter for width """
        return (self.__width)

    @width.setter
    def width(self, width):
        """validation of width"""
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getters and setter for Height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Validation of height"""
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getters and setter for x """
        return (self.__x)

    @x.setter
    def x(self, x):
        """validation of X"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getters and setter for y """
        return (self.__y)

    @y.setter
    def y(self, y):
        """ Validation of y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
