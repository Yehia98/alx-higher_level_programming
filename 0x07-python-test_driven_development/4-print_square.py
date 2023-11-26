#!/usr/bin/python3
"""module to print a square uing print_square() method"""


def print_square(size):
    """a method that prints a square of the character #.

    arges:
        size: is the size length of the square.

    raises:
        TypeError: if the size isn't an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print(("#" * size + "\n"), end="")
    

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
