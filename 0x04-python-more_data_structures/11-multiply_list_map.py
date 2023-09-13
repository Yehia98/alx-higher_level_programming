#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    product = list(map((lambda i: i * number), my_list))
    return (product)
