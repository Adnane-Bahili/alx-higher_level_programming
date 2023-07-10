#!/usr/bin/python3
"""defines an object attribute lookup function"""


def lookup(obj):
    """returns an object's available attributes list"""
    return (dir(obj))
