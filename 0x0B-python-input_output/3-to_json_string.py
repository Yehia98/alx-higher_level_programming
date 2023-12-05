#!/usr/bin/python3
"""a module of serialization"""


import json

def to_json_string(my_obj):
    """a function that converts an object into a JSON string"""
    json_string = json.dumps(my_obj)
    return json_string
