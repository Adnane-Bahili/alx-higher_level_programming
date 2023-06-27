#!/usr/bin/python3
"""translating the provided bytecode MagicClass"""
import math


class MagicClass:
    """represents a circle"""
    def __init__(self, radius=0):
        """initializes a MagicClass.
        argument:
            radius (float or int): new MagicClass radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns area of MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """returns circumference of MagicClass"""
        return (2 * math.pi * self.__radius)
