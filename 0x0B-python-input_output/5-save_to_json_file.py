#!/usr/bin/python3
"""defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using the JSON representation"""
    with open(filename, "w") as fl_n:
        json.dump(my_obj, fl_n)
