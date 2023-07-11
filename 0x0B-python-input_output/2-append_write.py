#!/usr/bin/python3
"""defines a file-appending function"""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file
    args:
        filename (str): name of file to append to
        text (str): string to append to the file
    return:
        characters appended count
    """
    with open(filename, "a", encoding="utf-8") as fl_n:
        return fl_n.write(text)
