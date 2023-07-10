#!/usr/bin/python3
"""defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object when possible
    arguments:
        obj (any): object to add an attribute to
        att (str): name of the attribute to add to the object
        value (any): attribute value
    raise:
        TypeError: when the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
