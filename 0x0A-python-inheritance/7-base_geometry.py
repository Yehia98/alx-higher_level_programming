#!/usr/bin/python3
"""a modulle of BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """an empty area fucntion"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """integer validator function"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
