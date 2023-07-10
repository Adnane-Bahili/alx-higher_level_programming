#!/usr/bin/python3
"""defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """intializes a new Rectangle.
        arguments:
            width (int): new Rectangle width
            height (int): new Rectangle height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns Rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """returns the "print()" and "str()" representation of the Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
