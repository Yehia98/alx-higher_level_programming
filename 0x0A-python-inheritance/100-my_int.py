#!/usr/bin/python3
"""a module of MyInt class"""


class MyInt(int):
    """MyInt class"""
    def __new__(cls, *args, **kwargs):
        """a new object"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """equal opt function"""
        return int(self) != other

    def __ne__(self, other):
        """not equal opt function"""
        return int(self) == other
