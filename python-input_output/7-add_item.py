#!/usr/bin/python3
""" Script that adds all arguments to a Python list """


from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    JSON_list = load_from_json_file(filename)
except:
    JSON_list = []

for arg in argv[1:]:
    JSON_list.append(arg)
save_to_json_file(JSON_list, filename)
