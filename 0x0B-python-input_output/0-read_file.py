#!/usr/bin/python3
"""defines a text file-reading function"""


def read_file(filename=""):
    """prints a UTF8 text file contents to the stdout"""
    with open(filename, encoding="utf-8") as fl_n:
        print(fl_n.read(), end="")
