#!/usr/bin/python3
"""a module of the square class thas inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """a friendly representation of the object items"""
        return '[Square] ({}) {}/{} - {}'.\
            format(self.id, self.x, self.y, self.width)
