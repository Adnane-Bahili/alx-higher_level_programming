#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """
    prevents user from initiating new LockedClass attributes
    for attributes that are other than "first_name"
    """
    __slots__ = ["first_name"]
