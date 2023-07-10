#!/usr/bin/python3
"""defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """represents the base geometry"""

    def area(self):
        """area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter as an integer
        arguments:
            name (str): parameter name
            value (int): parameter to validate
        raises:
            TypeError: when value is not an integer
            ValueError: when value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
