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

    @property
    def size(self):
        """size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def sq_arg_list(self, id=None, size=None, x=None, y=None):
        """unpacking **kw/*args into the instance attribute"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """a fucntion that assigns an argument to each attribute
        whether with keywords or not"""
        if args:
            self.sq_arg_list(*args)
        elif kwargs:
            self.sq_arg_list(**kwargs)
