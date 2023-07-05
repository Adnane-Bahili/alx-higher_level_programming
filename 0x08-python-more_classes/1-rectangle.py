#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, height=0, width=0):
        """initializes new rectangle
        arguments:
            height (int): new rectangle height
            width (int): new rectangle width
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get/set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
