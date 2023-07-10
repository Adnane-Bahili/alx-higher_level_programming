#!/usr/bin/python3
"""defines class MyInt that inherits from int"""


class MyInt(int):
    """inverts integer operators "==" and "!=" """

    def __eq__(self, value):
        """overrides the "==" opeartor with "!=" action"""
        return self.real != value

    def __ne__(self, value):
        """overrides the "!="" operator with "==" action"""
        return self.real == value
