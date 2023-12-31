#!/usr/bin/paython3
"""method say_my_name module"""


def say_my_name(first_name, last_name=""):
    """method for printing names

    args:
        first_name: first string
        last_name: second string

    raises:
        TypeError: if first_name or last_name are not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
