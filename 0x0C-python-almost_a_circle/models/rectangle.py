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
    
    def get_width(self):
        """Getters and setter for width """
            return (self.__width)
        
    def set_width(self, width):
        """validation of width"""
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """Getters and setter for Height"""
    def get_height(self):
        return (self.__width)

    def set_height(self, width):
        """Validation of height"""
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def get_x(self):
        """Getters and setter for x """
        return (self.__x)

    def set_x(self, x):
        """validation of X"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def get_y(self):
            """Getters and setter for y """
        return (self.__width)

    def set_y(self, y):
        """ Validation of y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        
