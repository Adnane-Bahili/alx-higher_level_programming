#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """represents rectangle
    attributes:
        number_of_instances (int): rectangle instances count
        print_symbol (any): string representation symbol
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes new rectangle
        arguments:
            width (int): new rectangle width
            height (int): new rectangle height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the rectangle with the superior area
        arguments:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        raise:
            TypeError: when "rect_1" or "rect_2" is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """returns new rectangle with height and width that's equal to size
        arguments:
            size (int): height and width of a new rectangle
        """
        return (cls(size, size))

    def __str__(self):
        """returns printed rectangle representation
        represents the rectangle with the "#" character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """returns rectangle string representation"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """printing a message for each rectangle deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
