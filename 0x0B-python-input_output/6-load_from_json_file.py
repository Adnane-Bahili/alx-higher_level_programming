#!/usr/bin/python3
"""defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """creates a Python object from a JSON file"""
    with open(filename) as fl_n:
        return json.load(fl_n)
