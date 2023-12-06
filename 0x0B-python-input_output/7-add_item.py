#!/usr/bin/python3
"""a module that adds all arguments to a Python list,
then save them to a file
"""


import sys
import json
import os.path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
j_list = []

if os.path.exists(file_name):
    j_list = load_from_json_file(file_name)

for i in argv[1:]:
    j_list.append(i)

save_to_json_file(j_list, file_name)
