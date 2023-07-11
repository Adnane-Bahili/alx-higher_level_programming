#!/usr/bin/python3
"""defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """returns a JSON string's Python object representation"""
    return json.loads(my_str)
