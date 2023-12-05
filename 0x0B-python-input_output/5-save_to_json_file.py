#!/usr/bin/python3
"""a module of a json string into a file"""


import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON"""
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
