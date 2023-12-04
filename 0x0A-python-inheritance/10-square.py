#!/usr/bin/python3
"""a module of square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass of Rectangle"""
    def __init__(self, size):
        """nstantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square area function"""
        return (self.__size ** 2)
