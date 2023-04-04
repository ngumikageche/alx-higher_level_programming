#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Intialize a new square.
        Args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Function that prints in stdout the square with the character #"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
