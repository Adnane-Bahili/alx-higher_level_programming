#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """prints name
    arguments:
        first_name (str): printable first name
        last_name (str): printable last name
    raise:
        TypeError: when first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
