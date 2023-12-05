#!/usr/bin/python3
"""a module of a write function into a file"""


def write_file(filename="", text=""):
    """a function that writes a string into a file"""
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(text)
    return (len(text))
