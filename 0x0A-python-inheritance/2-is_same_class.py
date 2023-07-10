#!/usr/bin/python3
"""defines a class-checking function"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a given class
    arguments:
        obj (any): The object to check.
        a_class (type): class to match the type of object to
    returns:
        True, when an object is exactly an instance of a_class
        False, otherwise
    """
    if type(obj) == a_class:
        return True
    return False
