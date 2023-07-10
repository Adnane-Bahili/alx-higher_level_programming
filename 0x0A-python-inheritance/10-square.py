#!/usr/bin/python3
"""defines Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents Square"""

    def __init__(self, size):
        """initializes a new Square
        argument:
            size (int): new square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
