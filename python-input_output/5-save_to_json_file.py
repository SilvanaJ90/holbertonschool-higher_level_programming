#!/usr/bin/python3
"""
Doc
"""
import json


def save_to_json_file(my_obj, filename):
    """ Write a function that writes an Object to a text file,
     using a JSON representation:"""

    with open('filename', 'w') as my_obj:
        return json.dumps(my_obj)
