#!/usr/bin/python3
"""a module of class dict"""


def class_to_json(obj):
    """a class dict for json serialization"""
    return obj.__dict__
