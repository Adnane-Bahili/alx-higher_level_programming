#!/usr/bin/python3
"""defines an inherited list class MyList"""


class MyList(list):
    """implements printing sorting for the built-in list class"""

    def print_sorted(self):
        """prints the list in an ascending order"""
        print(sorted(self))
