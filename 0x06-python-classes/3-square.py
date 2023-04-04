#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square."""
    # setter(mutator)
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): the size of the new square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
