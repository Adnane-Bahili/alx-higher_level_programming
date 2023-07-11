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

    def to_json(self):
        """get Student dictionary representation"""
        return self.__dict__
