#!/usr/bin/python3
"""a class that prints a list of an object"""


class MyList(list):
    """Mylist class to print a sorted list"""
    def print_sorted(self):
        """a function that prints a sorted list"""
        print(sorted(self))
