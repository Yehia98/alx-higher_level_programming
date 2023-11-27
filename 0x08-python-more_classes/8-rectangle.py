#!/usr/bin/python3
"""module that contains a Rectangle class"""


class Rectangle:
    """a blueprintate of a Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """class attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[:-1]

    def __repr__(self):
        """prints a developer friendly representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print message for deletion of an iinstance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the biggest area rectangle

        Args:
            rect_1: first rectangle.
            rect_2: 2nd rectangle.
            
        Raises:
                TypeError: if rect_1 or rect_2 are not instances
                of Rectangel
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

        if rect_2.area() == rect_1.area():
            return rect_1
