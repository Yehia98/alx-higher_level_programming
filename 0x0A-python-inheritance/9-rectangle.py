#!/usr/bin/python3
"""a module of Rectangle subclass"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a sub class of BaseGeometry super class"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """a function that calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """printing a string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
