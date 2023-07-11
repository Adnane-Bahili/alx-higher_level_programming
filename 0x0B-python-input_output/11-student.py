#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """represents student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new Student
        arguments:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get Student dictionary representation
        when "attrs" is a list of strings,
        represents the attributes included in the list only
        argument:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces attributes of the Student
        argument:
            json (dict): key/value pairs to replace attributes with
        """
        for key, val in json.items():
            setattr(self, key, val)
