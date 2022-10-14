#!/usr/bin/python3
"""
Doc
"""


import re


def write_file(filename="", text=""):
    """ Doc """
    text = "This School is so cool!\n"
    with open("my_first_file.txt", mode="w", encoding="utf-8") as filename:
        filename.write(text)
    print(len(text))
   
