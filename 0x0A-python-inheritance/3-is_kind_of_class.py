#!/usr/bin/python3
"""defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance or inherited instance of a class
    arguments:
        obj (any): object to check
        a_class (type): class to match the type of object to
    returns:
        True, when an object is an instance or inherited instance of a_class
        False, otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
