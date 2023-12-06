#!/usr/bin/python3
"""a module of a student class"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """a function that replaces the current dict"""
        for key, value in json.items():
            setattr(self, key, value)
