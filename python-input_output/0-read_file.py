#!/usr/bin/python3
"""
Doc
"""


def read_file(filename=""):
    """ Doc """
    with open(filename, encoding="utf-8") as f:
        print(f.read())