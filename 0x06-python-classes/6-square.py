#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Intialize a new square.
        Args:
            size (int): the size of the new square.
        """
        self.size = size
        self.__position = position

    @property
    def position(self):
        """retrieves the position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the value returned"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
