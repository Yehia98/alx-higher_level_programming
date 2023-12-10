#!/usr/bin/python3
"""a module of the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """x attribute getter"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """y attribute getter"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """computing the rectangle area"""
        return self.width * self.height

    def display(self):
        """a function that prints the Rectangle with the character #"""
        display = '\n' * self.y + \
                  (' ' * self.x + '#' * self.width + '\n') * self.height
        print(display, end=" ")

    def __str__(self):
        """user friendly representation of the object items"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.\
            format(self.id, self.x, self.y, self.width, self.height)

    def arg_list(self, id=None, width=None, height=None, x=None, y=None):
        """unpacking **kw/*args into the instance attribute"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """a fucntion that assigns an argument to each attribute
        whether with keywords or not"""
        if args:
            self.arg_list(*args)
        elif kwargs:
            self.arg_list(**kwargs)
