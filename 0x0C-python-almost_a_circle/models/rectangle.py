#!/usr/bin/python3
from models.base import Base
"""Defines a class rectangle"""


class Rectangle(Base):
    """body of rectangle"""
    def __init__(self, width, height, x = 0, y = 0, id = None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Getters and setter for width """
    def get_width(self):
            return (self.__width)
    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """Getters and setter for Height"""
    def get_height(self):
        return (self.__width)

    def set_height(self, width):
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """Getters and setter for x """
    def get_x(self):
        return (self.__x)

    def set_x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """Getters and setter for y """
    def get_y(self):
        return (self.__width)

    def set_y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        
