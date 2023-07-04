#!/usr/bin/python3
def print_square(size):
    """prints a square using the # character
    argument:
        size (int): length and width of the square
    raises:
        TypeError: when size is not an integer
        ValueError: when the size is below 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for s in range(size):
        [print("#", end="") for t in range(size)]
        print("")
