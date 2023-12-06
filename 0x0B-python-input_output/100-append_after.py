#!/usr/bin/python3
"""a module of appending a text file"""


def append_after(filename="", search_string="", new_string=""):
    """ that inserts a line of text to a file,after each line """
    with open(filename, "r", encoding="utf-8") as file:
        S_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            S_list.append(line)
            if search_string in line:
                S_list.append(new_string)
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(S_list)
