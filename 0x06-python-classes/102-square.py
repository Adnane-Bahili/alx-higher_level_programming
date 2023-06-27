#!/usr/bin/python3
"""defines class square"""


class Square:
    """represents square"""
    def __init__(self, size=0):
        """initializes new square
        argument:
            size (int): new square size
        """
        self.size = size

    @property
    def size(self):
        """get/set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns current area of square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """defines the "==" comparison to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """defines the "!=" comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """defines the "<" comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """defines the "<=" comparison to a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """defines the ">" comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """defines the ">=" compmarison to a square"""
        return self.area() >= other.area()
