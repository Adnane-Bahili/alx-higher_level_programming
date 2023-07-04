#!/usr/bin/python3
def add_integer(a, b=98):
    """returns the addition of a and b
    float arguments are typecasted to integers before addition
    raise:
        TypeError: when a or b is not an integer and not a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
