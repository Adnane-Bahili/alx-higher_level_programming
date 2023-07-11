#!/usr/bin/python3
"""defines a Python class-to-JSON function"""


def class_to_json(obj):
    """returns the dictionary represntation of a simple data structure"""
    return obj.__dict__
