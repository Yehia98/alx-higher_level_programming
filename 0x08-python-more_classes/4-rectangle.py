#!/usr/bin/python3
"""module that contains a Rectangle class"""


class Rectangle:
    """a blueprintate of a Rectangle class"""
    def __init__(self, width=0, height=0):
        """class attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public method that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints a user friendly representation"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += '\n'.join('#' * self.__width
                                for x in range(self.__height))
        return string

    def __repr__(self):
        """prints a developer friendly representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
