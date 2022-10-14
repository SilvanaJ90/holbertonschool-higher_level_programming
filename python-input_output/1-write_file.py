#!/usr/bin/python3
"""
Doc
"""


def write_file(filename="", text=""):
    """ Doc """
    with open("my_first_file.txt", mode="w", encoding="utf-8") as filename:
        filename.write(text)
    print(len(text))
   
