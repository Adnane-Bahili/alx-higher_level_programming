#!/usr/bin/python3
"""defines a file-writing function"""


def write_file(filename="", text=""):
    """writes a string to a UTF8 text file
    arguments:
        filename (str): name of file to write to
        text (str): string to write to the file
    return:
        characters written count
    """
    with open(filename, "w", encoding="utf-8") as fl_n:
        return fl_n.write(text)
