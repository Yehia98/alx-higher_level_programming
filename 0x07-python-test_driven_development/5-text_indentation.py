#!/usr/bin/python3
"""module that indent a text"""


def text_indentation(text):
    """method that applies text indentation

    args:
        text: a string.

    raises:
        TypeError: if text isn't a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for sym in ".?:":
        words = (sym + "\n\n").join(
              [index.strip(" ") for index in words.split(sym)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.py")
