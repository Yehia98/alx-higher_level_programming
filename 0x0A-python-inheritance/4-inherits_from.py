#!/usr/bin/python3
"""a module that checks the origin of an object"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class"""
    return isinstance(obj, a_class) and type(obj) != a_class
