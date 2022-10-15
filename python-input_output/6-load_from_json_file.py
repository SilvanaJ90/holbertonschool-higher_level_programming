#!/usr/bin/python3
"""
Doc
"""

import json


def load_from_json_file(filename):
    """ Write a function that creates an Object from a “JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
