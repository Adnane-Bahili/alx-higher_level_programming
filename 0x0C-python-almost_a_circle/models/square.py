#!/usr/bin/python3
"""defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a new Square.
        arguments:
            size (int): size of the new Square
            x (int): x coordinate of the new Square
            y (int): y coordinate of the new Square
            id (int): new Square id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kw_args):
        """updates the Square
        arguments:
            *args (ints): New attribute values
                - 1st argument representing id attribute
                - 2nd argument representing size attribute
                - 3rd argument representing x attribute
                - 4th argument representing y attribute
            **kw_args (dict): New key/value  attributes pairs
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kw_args and len(kw_args) != 0:
            for k, v in kw_args.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the Square dictionary representation"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

        def __str__(self):
            """returns the Square "print()" and "str()" representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
