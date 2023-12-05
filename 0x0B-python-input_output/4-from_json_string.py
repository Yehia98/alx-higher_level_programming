#!/usr/bin/python3
"""a module of deserialization"""


import json


def from_json_string(my_str):
    """a function that converts a json string into a py object"""
    py_obj = json.loads(my_str)
    return py_obj
