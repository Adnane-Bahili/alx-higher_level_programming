#!/usr/bin/python3
"""defines class square"""


class Square:
    """represents square"""
    def __init__(self, size):
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
        """returns current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square with "#" character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
