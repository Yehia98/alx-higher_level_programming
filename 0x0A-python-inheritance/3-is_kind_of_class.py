#!/usr/bin/python3
"""a module that checks if the object is exactly an instance of a class"""


def is_kind_of_class(obj, a_class):
    """a function that checks if the object is exactly an
    instance of a specified class"""
    return isinstance(obj, a_class)
