#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_keys = list(a_dictionary.keys())
    new_keys.sort()
    for i in new_keys:
        print('{}: {}' .format(i, a_dictionary.get(i)))
