#!/usr/bin/python3
"""defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a class
    arguments:
        obj (any): object to check
        a_class (type): class to match the type of object to
    returns:
        True, when an object is an inherited instance of a_class
        False, otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
