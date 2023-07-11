#!/usr/bin/python3
"""defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts text after each line that contains a specific string in a file
    arguments:
        filename (str): file name
        search_string (str): string to search for
        new_string (str): string to insert
    """
    new_str = ""
    with open(filename) as f:
        for line in f:
            new_str += line
            if search_string in line:
                new_str += new_string
    with open(filename, "w") as w:
        w.write(new_str)
