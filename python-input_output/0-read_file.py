#!/usr/bin/python3
"""
Doc
"""


def read_file(filename=""):
    """ Doc """
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")
