#!/usr/bin/python3
"""
Doc
"""
from distutils.file_util import move_file
import json


def load_from_json_file(filename):
    """ Write a function that creates an Object from a “JSON file"""
    with open(filename, 'w') as outfile:
        json.load(filename, outfile)
