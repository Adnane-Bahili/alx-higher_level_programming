#!/usr/bin/python3
"""defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """intializes new Rectangle

        arguments:
            width (int): new Rectangle width
            height (int): new Rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
