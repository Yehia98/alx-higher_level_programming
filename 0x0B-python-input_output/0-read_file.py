#!/usr/bin/python3
"""a modue of a file read function"""


def read_file(filename=""):
    """a function that reads the contents of a file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read())
