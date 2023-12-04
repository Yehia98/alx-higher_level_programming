#!/usr/bin/python3
"""a module of rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass of Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ square area function"""
        return (self.__size ** 2)

    def __str__(self):
        """prints the string of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
